# Adopt v0.3 from v0.2

Review ADR-0025 through ADR-0027 and classify the 12 new CQRS, middleware and OpenAPI rules. Existing pinned applications are unchanged until adoption.

Map current use cases to command/query responsibilities; do not introduce separate databases or a mediator just to comply. Inspect the actual host pipeline and verify ordering through real requests. Choose one OpenAPI generator and migrate any duplicate document sources; verify UI/dialect/client compatibility and production exposure. Update contract parity tests before replacing generation tooling. Preserve endpoint IDs and supported schemas.

Adopt the new immutable commit and baselineVersion 0.3.0 with the normal manifest/evidence process. CORS remains conditional on browser origins. Runtime snippets remain illustrative until the consuming application builds and tests them.
