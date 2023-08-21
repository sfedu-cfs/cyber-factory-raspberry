# Cyber Factory Raspberry

__TODO:__ _Do all executables in Makefile, e.g._

- install dependencies `make install`
- run tests `make test`
- run analyzers `make run network_analyzer` _etc_

## Quick start

Install pipenv:

```bash
python3 -m pip install pipenv
```

Install dependencies:

```bash
pipenv install
```

Activate pipenv shell:

```bash
pipenv shell
```

## Run analyzers

### Network analyzer

```bash
python3 network_analyzer.py
```

### System analyzer

```bash
python3 system_analyzer.py
```

### System resources analyzer

```bash
python3 sys_resources_analyzer.py
```

## Tests

For run tests:

```bash
pytest 
```

