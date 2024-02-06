# standard library
import os

# third party library
from dotenv import load_dotenv


load_dotenv()


class BaseConfig:
    """基本配置"""

    TESTING = False
    DEBUG = False
    SECRET_KEY = os.getenv("SECRET_KEY", default="BAD_SECRET_KEY")


class DevelopmentConfig(BaseConfig):
    """開發階段配置"""

    SQLALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_DATABASE_URI_DEVELOPMENT")
    DEBUG = True


class DockerDevelopmentConfig(BaseConfig):
    """Docker開發階段配置"""

    SQLALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_DATABASE_URI_DOCKER_DEVELOPMENT")
    DEBUG = True

class ProductionConfig(BaseConfig):
    """生產階段配置"""

    SQLALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_DATABASE_URI_PRODUCTION")


class TestingConfig(BaseConfig):
    """測試階段配置"""

    SQLALCHEMY_DATABASE_URI = "sqlite://"
    TESTING = True
