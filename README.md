# Unit Testing (Pytest)

- Function based testing
- Class based testing
- Mark (skip, xfail)
- Parametrize
- Mocking

## Pre-requisites

```bash
pip install -r requirements.txt
```

## Command

To run all the test-functions of the file
```bash
pytest <test_file-name>
```
\
To run a single test-function
```bash
pytest -k <test-function-name>
```
\
To debug (or to run print statements), use `-s`

```bash
pytest -s <test_file-name>
```

\
For verbose
```bash
pytest -v <test_file-name>
```
---

> [!Note]
> We can create a file `pytest.ini` to add options/flag for pytest command so that we do not need to provide it at as command line argument.
