# hyper-python

## requirements

### pyenv
```bash
pyenv virtualenv hyper-python
pyenv activate hyper-python
```

### poetry
```bash
pipx install poetry
```

## setup

### install packages
```bash
poetry install
```

### run - console
```bash
poetry run hyper-python
```
#### run - console - language
```bash
poetry run hyper-python --langauge fr 
```
```bash
poetry run hyper-python -l fr 
```

### test
```bash
poetry run pytest --cov
```