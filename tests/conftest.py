# standard libraray
import os

# third party library
import pytest
from flask import Flask
from flask.testing import FlaskClient, FlaskCliRunner
from flask_sqlalchemy import SQLAlchemy
from werkzeug.datastructures import ImmutableDict

# local library
from app import create_app, db
from app.models.volunteer import Volunteer
from app.tools import generate


@pytest.fixture(scope="session")
def app() -> Flask:
    """產生一個測試用的 app
    """
    os.environ["CONFIG_TYPE"] = "config.TestingConfig"
    app = create_app()
    yield app  # 測試發生處


@pytest.fixture(scope="session")
def test_client(app: Flask) -> FlaskClient:
    """產生一個測試用的 client
    """
    with app.test_client() as testing_client:
        with app.app_context():
            yield testing_client # 測試發生處


@pytest.fixture(scope="module")
def cli_test_client(app: Flask) -> FlaskCliRunner:
    runner = app.test_cli_runner()
    yield runner # 測試發生處


@pytest.fixture(scope="function", name="db")
def init_database(test_client: FlaskClient) -> SQLAlchemy:
    """資料庫創建/刪除上下文
    """
    db.create_all() # 資料庫創建所有資料表
    yield db        # 測試發生處
    db.drop_all()   # 資料庫刪除所有資料表


@pytest.fixture(scope="function")
def new_volunteer() -> Volunteer:
    """產生一個填表者
    """
    return Volunteer(
        ImmutableDict(
        [
            ("formID", "233635142103444"),
            (
                "jsExecutionTracker",
                "build-date-1704013390989=>init-started:1704018466372=>validator-called:1704018466378=>validator-mounted-true:1704018466378=>init-complete:1704018466381=>interval-complete:1704018487387=>onsubmit-fired:1704018492697=>submit-validation-passed:1704018492700",
            ),
            ("submitSource", "form"),
            ("buildDate", "1704013390989"),
            ("HighBP", "1"),
            ("HighChol", "1"),
            ("CholCheck", "0"),
            ("Smoker", "0"),
            ("Stroke", "1"),
            ("HeartDiseaseorAttack", "0"),
            ("PhysActivity", "1"),
            ("Fruits", "0"),
            ("Veggies", "1"),
            ("HvyAlcoholConsump", "0"),
            ("AnyHealthcare", "1"),
            ("NoDocbcCost", "0"),
            ("DiffWalk", "1"),
            ("Sex", "0"),
            ("BMI", "30"),
            ("Age", "40"),
            ("Education", "6"),
            ("Income", "11"),
            ("GenHlth", "3"),
            ("MentHlth", "20"),
            ("PhysHlth", "12"),
            ("EmailAddress", "testvolunteer@gmail.com"),
            ("formOpenId_V5", "14999403757376451606"),
            ("timeToSubmit", "20"),
            ("event_id", "1704018466380_233635142103444_9Ev2l4U"),
            ("validatedNewRequiredFieldIDs", '{"new":1}'),
        ]
    )
)


@pytest.fixture(scope="function")
def add_dummy_volunteers(db: SQLAlchemy) -> None:
    """產生10個隨機填表者並填入資料庫
    """
    volunteers = [Volunteer(generate.random_form()) for _ in range(1, 10)]
    for volunteer in volunteers:
        volunteer.predict()
    db.session.add_all(volunteers)
    db.session.commit()

