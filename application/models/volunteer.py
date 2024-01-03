# standard library
import datetime
import uuid
from typing import Any
import itertools

# third party library
from sqlalchemy import Column, Integer, Text, DateTime, Float, UUID
import pandas as pd

# local library
from application import db, MODEL_PRETRAINED


class Volunteer(db.Model):
    __tablename__ = "volunteer"

    # other_columns
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    buildDate = Column(DateTime)
    EmailAddress = Column(Text)

    # data_columns
    HighBP = Column(Integer, nullable=False)
    HighChol = Column(Integer, nullable=False)
    CholCheck = Column(Integer, nullable=False)
    BMI = Column(Integer, nullable=False)
    Smoker = Column(Integer, nullable=False)
    Stroke = Column(Integer, nullable=False)
    HeartDiseaseorAttack = Column(Integer, nullable=False)
    PhysActivity = Column(Integer, nullable=False)
    Fruits = Column(Integer, nullable=False)
    Veggies = Column(Integer, nullable=False)
    HvyAlcoholConsump = Column(Integer, nullable=False)
    AnyHealthcare = Column(Integer, nullable=False)
    NoDocbcCost = Column(Integer, nullable=False)
    GenHlth = Column(Integer, nullable=False)
    MentHlth = Column(Integer, nullable=False)
    PhysHlth = Column(Integer, nullable=False)
    DiffWalk = Column(Integer, nullable=False)
    Sex = Column(Integer, nullable=False)
    Age = Column(Integer, nullable=False)
    Education = Column(Integer, nullable=False)
    Income = Column(Integer, nullable=False)

    # result_columns
    Stage0_Reliabilities = Column(Float(8), nullable=False)
    Stage1_Reliabilities = Column(Float(8), nullable=False)
    Stage2_Reliabilities = Column(Float(8), nullable=False)

    other_columns = tuple(
        [
            "id", 
            "buildDate", 
            "EmailAddress"
        ]
    )

    data_columns = tuple(
        [
            "HighBP",
            "HighChol",
            "CholCheck",
            "BMI",
            "Smoker",
            "Stroke",
            "HeartDiseaseorAttack",
            "PhysActivity",
            "Fruits",
            "Veggies",
            "HvyAlcoholConsump",
            "AnyHealthcare",
            "NoDocbcCost",
            "GenHlth",
            "MentHlth",
            "PhysHlth",
            "DiffWalk",
            "Sex",
            "Age",
            "Education",
            "Income",
        ]
    )

    result_columns = tuple(
        [
            "Stage0_Reliabilities",
            "Stage1_Reliabilities",
            "Stage2_Reliabilities"
        ]
    )

    def __init__(self, **kwargs: Any) -> None:
        """填表者 database table

        初始化時，僅將存在於 `Volunteer.data_columns` 與 `Volunteer.other_columns` 的名稱設置屬性，
        並必須手動將預測結果賦值給 `Volunteer.result_columns` 中的三個屬性，
        以上皆完成後才能將這筆資料存入資料庫。
        """
        for column in Volunteer.data_columns:
            if column == "BMI":  # 浮點數
                setattr(self, column, float(kwargs[column]))
            else:
                setattr(self, column, int(kwargs[column]))
        for column in Volunteer.other_columns:
            if column == "id":  # 預設值
                pass
            elif column == "buildDate":  # 時間戳
                setattr(self, column, datetime.datetime.utcfromtimestamp(float(kwargs[column]) / 1000))
            else:
                setattr(self, column, str(kwargs[column]))

    def jsonify(self) -> dict[str, Any]:
        """轉為 JSON 格式

        Returns
        -------
        `volunteer_dict` (dict[str, Any])
        """
        volunteer_dict = dict()
        for column in itertools.chain(
            Volunteer.data_columns, Volunteer.other_columns, Volunteer.result_columns
        ):
            try:
                volunteer_dict[column] = getattr(self, column)
            except AttributeError:
                volunteer_dict[column] = None
        return volunteer_dict

    def standardize(self) -> pd.DataFrame:
        """產生可直接丟入模型 predict 的資料

        Returns
        -------
        `data` (pd.DataFrame)
        """
        volunteer_dict = self.jsonify()
        for column in Volunteer.other_columns:
            volunteer_dict.pop(column)
        for column in Volunteer.result_columns:
            try:
                volunteer_dict.pop(column)
            except KeyError:
                pass
        data = pd.DataFrame(volunteer_dict, index=[0])
        return data

    def predict(self) -> None:
        """模型預測，並將結果設置於 `Volunteer.result_columns` 中的三個屬性。"""
        data = self.standardize()
        result_probas = map(float, MODEL_PRETRAINED.predict_proba(data)[0])
        for column, result_proba in zip(Volunteer.result_columns, result_probas):
            setattr(self, column, result_proba)
