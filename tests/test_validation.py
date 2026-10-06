"""Negative cases ensure documentation/evidence gates catch meaningful omissions."""
from copy import deepcopy
from datetime import date
import importlib.util
import json
from pathlib import Path
import shutil
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
def load(name):
    spec = importlib.util.spec_from_file_location(name, ROOT/'scripts'/f'{name}.py')
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

adoption = load('check_adoption')
docs = load('validate')

class AdoptionTests(unittest.TestCase):
    def setUp(self):
        self.catalog = {'version':'0.2.0','rules':[{'id':'CORS-001'},{'id':'DB-001'}]}
        self.baseline = {'standardsRepository':'https://github.com/example/standards',
            'standardsRevision':'a'*40,'baselineVersion':'0.2.0','solutionDocument':'docs/solution.md',
            'applicationKind':'frontend','adoptionRecord':{'owner':'Fixture owner','date':'2026-10-05','evidence':'docs/adoption.md'},
            'applicableRules':['CORS-001'],'excludedRules':[{'rule':'DB-001','reason':'No database in client repo'}],
            'acceptedExceptions':[]}
        self.evidence = {'standardsRevision':'a'*40,'baselineVersion':'0.2.0','applicationCommit':'b'*40,
            'checks':[{'rule':'CORS-001','status':'passed','method':'Fixture browser test','evidence':'reports/fixture.json'}]}
    def check(self, release=False):
        return adoption.validate_adoption(self.catalog,self.baseline,self.evidence,release,date(2026,10,6))
    def test_complete_fixture(self):
        self.assertEqual([],self.check(True))
    def test_missing_rule_disposition(self):
        self.baseline['excludedRules']=[]
        self.assertTrue(any('Coverage mismatch' in e for e in self.check()))
    def test_missing_evidence(self):
        self.evidence['checks']=[]
        self.assertTrue(any('Missing evidence' in e for e in self.check()))
    def test_no_empty_pass_claim(self):
        del self.evidence['checks'][0]['method']
        self.assertTrue(any('requires method' in e for e in self.check()))
    def test_no_mutable_revision(self):
        self.baseline['standardsRevision']='main'
        self.assertTrue(any('immutable' in e for e in self.check()))
    def test_wrong_baseline_evidence(self):
        self.evidence['standardsRevision']='c'*40
        self.assertTrue(any('differs' in e for e in self.check()))
    def test_not_run_is_not_release_success(self):
        self.evidence['checks'][0]={'rule':'CORS-001','status':'not_run','reason':'Browser unavailable'}
        self.assertEqual([],self.check())
        self.assertTrue(any('Release gate' in e for e in self.check(True)))
    def test_expired_exception(self):
        self.baseline['acceptedExceptions']=[{'id':'EX-1','rules':['CORS-001'],'status':'Accepted',
            'owner':'Fixture owner','approvalEvidence':'docs/approval.md','reason':'Fixture deviation',
            'remediation':'issues/1','expires':'2026-10-05'}]
        self.evidence['checks'][0]={'rule':'CORS-001','status':'excepted','exceptionId':'EX-1'}
        self.assertTrue(any('expired' in e for e in self.check(True)))
    def test_unapproved_exception(self):
        self.evidence['checks'][0]={'rule':'CORS-001','status':'excepted','exceptionId':'EX-missing'}
        self.assertTrue(any('covering accepted' in e for e in self.check()))
    def test_duplicate_rule_check(self):
        self.evidence['checks'].append(deepcopy(self.evidence['checks'][0]))
        self.assertTrue(any('Duplicate evidence' in e for e in self.check()))

class DocumentationTests(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory()
        self.root=Path(self.tmp.name)/'repo'
        shutil.copytree(ROOT,self.root,ignore=shutil.ignore_patterns('__pycache__','.git'))
    def tearDown(self):
        self.tmp.cleanup()
    def test_broken_local_link(self):
        with (self.root/'README.md').open('a') as f:f.write('\n[Missing](missing.md)\n')
        self.assertTrue(any('Broken link' in e for e in docs.validate(self.root)))
    def test_unknown_rule(self):
        with (self.root/'README.md').open('a') as f:f.write('\nRule FAKE-999\n')
        self.assertTrue(any('Unknown rule' in e for e in docs.validate(self.root)))
    def test_false_accepted_provenance(self):
        file=self.root/'standards/catalog.json';cat=json.loads(file.read_text())
        next(r for r in cat['rules'] if r['id']=='CORS-001')['status']='Accepted'
        file.write_text(json.dumps(cat))
        self.assertTrue(any('non-accepted ADR' in e for e in docs.validate(self.root)))
    def test_missing_rule_table_entry(self):
        file=self.root/'security/cors-standard.md'
        file.write_text(file.read_text().replace('| CORS-001 |','| Removed |'))
        self.assertTrue(any('missing from document' in e for e in docs.validate(self.root)))

if __name__ == '__main__':unittest.main()
