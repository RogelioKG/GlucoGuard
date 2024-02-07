@echo off
call .venv\Scripts\activate
coverage run -m pytest -v -s --disable-warnings