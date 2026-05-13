<!-- Thanks for the PR! Brief context here. -->

## What this changes

<!-- 1-3 bullet points -->

## Why

<!-- Link the issue if one exists, or explain the user-facing reason. -->

## Test plan

- [ ] `pytest -v -m "not e2e"` passes locally
- [ ] `ruff check .` clean
- [ ] `pyright src tests` clean
- [ ] Manually exercised the affected CLI command in a `/tmp/cm-test` project
- [ ] Added/updated tests in `tests/unit/`
- [ ] `CHANGELOG.md` updated under `[Unreleased]` (for user-visible changes)

## Notes for reviewer

<!-- Anything tricky, intentional trade-offs, follow-up work split into separate PRs, etc. -->
