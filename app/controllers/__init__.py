from flask import Blueprint

basic_blueprint = Blueprint("basic", __name__)

from . import basic_controllers

__all__ = [
    "basic_controllers"
]
