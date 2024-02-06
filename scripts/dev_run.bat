@echo off
call .venv\Scripts\activate
set "CONFIG_TYPE=config.DevelopmentConfig"
flask --app app --debug run