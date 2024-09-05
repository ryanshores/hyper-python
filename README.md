# hyper-python

## requirements

### pyenv
```bash
pyenv install 3.12
pyenv virtualenv 3.12 hyper-python
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
poetry run hyper-python --language fr 
```
```bash
poetry run hyper-python -l fr 
```

### test
```bash
poetry run pytest --cov
```