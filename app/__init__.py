# standard library
import os

# third party library
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# 資料庫
db = SQLAlchemy()


def create_app() -> Flask:
    """
    Flask 工廠模式
    """
    app = Flask(__name__)

    # 應用程式配置
    config_type = os.getenv("CONFIG_TYPE", default="config.DevelopmentConfig")
    app.config.from_object(config_type)

    # 資料庫初始化
    db.init_app(app)

    # 應用程式註冊藍圖
    register_blueprints(app)

    # 應用程式註冊 CLI 指令
    register_cli_commands(app)

    # 資料庫創建資料表
    with app.app_context():
        db.create_all()
        app.logger.info("Initialized the database.")

    app.logger.info("Creating the app.")

    return app


def register_blueprints(app: Flask) -> None:
    from .controllers import basic_blueprint

    app.register_blueprint(basic_blueprint)


def register_cli_commands(app: Flask) -> None:
    from .tools.commands import db_cli
    
    app.cli.add_command(db_cli)
