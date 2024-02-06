@echo off
call .venv\Scripts\activate
set "CONFIG_TYPE=config.TestingConfig"
coverage run --rcfile=tests\pytest.ini -m pytest -v