poetry install
poetry run pytest --cov
pylint hyper_python
black hyper_python