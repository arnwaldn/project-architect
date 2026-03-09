---
name: test-plugin
description: Run the 10 integration tests for the project-architect plugin (structure, matrix, questions, cache, templates, installation)
disable-model-invocation: true
---

# Test Plugin

Execute the full integration test suite and report results.

## Instructions

1. Run the test suite:

```bash
python "C:/Users/arnau/Documents/projets/skill project-architect/data/test-all.py"
```

2. Report the results:
   - Show the full output (10 tests)
   - Highlight any FAIL or ERROR
   - If all 10 pass, confirm with ALL TESTS PASSED
   - If any fail, list the specific errors and suggest fixes
