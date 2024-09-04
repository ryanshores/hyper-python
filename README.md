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

### test
```bash
poetry run pytest --cov
```