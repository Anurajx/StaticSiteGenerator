## Test Coverage

The project is tested using Python's `coverage` module.

```bash
python3 -m coverage report -m
```

### Coverage Summary

| File                          | Coverage |
| ----------------------------- | -------: |
| `blockElements.py`            | **100%** |
| `delimiters.py`               | **100%** |
| `htmlnode.py`                 |      84% |
| `main.py`                     |      86% |
| `regexExtract.py`             |      94% |
| `textnode.py`                 |      80% |
| `tests/test_blockElements.py` | **100%** |
| `tests/test_delimiter.py`     |      97% |
| `tests/test_htmlnode.py`      |      99% |
| `tests/test_main.py`          | **100%** |
| `tests/test_regex.py`         | **100%** |
| `tests/test_textnode.py`      |      98% |

### Overall Coverage

| Metric               |   Value |
| -------------------- | ------: |
| Total Statements     |     452 |
| Missed Statements    |      24 |
| **Overall Coverage** | **95%** |

### Coverage Report

```text
Name                          Stmts   Miss  Cover
-------------------------------------------------
blockElements.py                 34      0   100%
delimiters.py                    17      0   100%
htmlnode.py                      50      8    84%
main.py                          14      2    86%
regexExtract.py                  50      3    94%
tests/test_blockElements.py      24      0   100%
tests/test_delimiter.py          30      1    97%
tests/test_htmlnode.py           76      1    99%
tests/test_main.py               18      0   100%
tests/test_regex.py              48      0   100%
tests/test_textnode.py           51      1    98%
textnode.py                      40      8    80%
-------------------------------------------------
TOTAL                           452     24    95%
```
