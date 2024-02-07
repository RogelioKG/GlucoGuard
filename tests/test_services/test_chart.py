# third party library
import pytest
from flask_sqlalchemy import SQLAlchemy

# local library
from app.services import chart


@pytest.mark.skip(reason="#todo")
@pytest.mark.usefixtures("add_dummy_volunteers")
def test_count_bar_chart(db: SQLAlchemy):
    pass