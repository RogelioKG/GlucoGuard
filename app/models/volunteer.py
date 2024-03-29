# standard library
import datetime
import itertools
import random
import time
import string
from typing import Any, Generator

# third party library
import pandas as pd
from sqlalchemy import Column, Integer, Text, DateTime, Float

# local library
from app import db
from app.constants import MODEL_PRETRAINED
from app.models import BaseDataModel
from app.tools.generate import truncated_gauss


class Volunteer(db.Model, BaseDataModel):
    __tablename__ = "volunteer"

    # other_columns
    id = Column(Integer, primary_key=True)
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

    other_columns = (
        "id",
        "buildDate",
        "EmailAddress"
    )

    data_columns = (
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
        "Income"
    )

    result_columns = (
        "Stage0_Reliabilities",
        "Stage1_Reliabilities",
        "Stage2_Reliabilities"
    )

    def __init__(self, form: dict[str, Any]) -> None:
        """填表者資料結構

        Parameters
        ----------
        + `form` (dict[str, Any]) : 表單
            - `key` (str) : 只將存在於 `Volunteer.data_columns` 與 `Volunteer.other_columns` 的欄位設值
            - `value` (Any) : 對應值

        Caution
        -------
        初始化時，沒有設置的欄位預設為 None。
        初始化後，需再進行預測，方可填入資料庫。

        ```py
        >>> volunteer = Volunteer(form) # 實例產生 (未含預測結果)
        >>> volunteer.predict()         # 模型預測 (填入預測結果)
        >>> db.session.add(volunteer)   # 資料庫操作
        >>> db.session.commit()
        ```
        """
        for column in Volunteer.data_columns:
            if column == "BMI":  # 浮點數
                setattr(self, column, float(form[column]))
            else:
                setattr(self, column, int(form[column]))
        for column in Volunteer.other_columns:
            if column == "id":
                pass
            elif column == "buildDate":  # 時間戳 (unix time ms)
                setattr(self, column, datetime.datetime.utcfromtimestamp(float(form[column]) / 1000))
            else:
                setattr(self, column, str(form[column]))

    def __repr__(self) -> str:
        return pd.Series(self.jsonify()).to_string()

    def jsonify(self) -> dict[str, Any]:
        """轉為類 JSON 物件

        Returns
        -------
        `volunteer_dict` (dict[str, Any])
        """
        volunteer_dict = {
            column: getattr(self, column)
            for column in itertools.chain(
                Volunteer.data_columns,
                Volunteer.other_columns,
                Volunteer.result_columns,
            )
        }

        return volunteer_dict

    def standardize(self) -> pd.DataFrame:
        """產生可直接丟入模型 predict 的資料

        Returns
        -------
        `data` (pd.DataFrame)
        """
        volunteer_dict = self.jsonify()
        for column in itertools.chain(
            Volunteer.other_columns, Volunteer.result_columns
        ):
            volunteer_dict.pop(column)
        data = pd.DataFrame(volunteer_dict, index=[0])
        return data

    def predict(self) -> None:
        """將實例丟入模型預測

        將 `Volunteer.result_columns` 中的欄位設值 (預測結果)
        """
        data = self.standardize()
        result_probas = map(float, MODEL_PRETRAINED.predict_proba(data)[0])
        for column, result_proba in zip(Volunteer.result_columns, result_probas):
            setattr(self, column, result_proba)

    @staticmethod
    def generate(n: int) -> Generator["Volunteer", Any, None]:
        """生成 n 筆隨機資料

        Parameters
        ----------
        + `n` (int)
        """
        for _ in range(n):
            volunteer_dict = {
                "buildDate": str(int(time.time() * 1000)), # unixtime (ms)
                "HighBP": str(random.randint(0, 1)),
                "HighChol": str(random.randint(0, 1)),
                "CholCheck": str(random.randint(0, 1)),
                "Smoker": str(random.randint(0, 1)),
                "Stroke": str(random.randint(0, 1)),
                "HeartDiseaseorAttack": str(random.randint(0, 1)),
                "PhysActivity": str(random.randint(0, 1)),
                "Fruits": str(random.randint(0, 1)),
                "Veggies": str(random.randint(0, 1)),
                "HvyAlcoholConsump": str(random.randint(0, 1)),
                "AnyHealthcare": str(random.randint(0, 1)),
                "NoDocbcCost": str(random.randint(0, 1)),
                "DiffWalk": str(random.randint(0, 1)),
                "Sex": str(random.randint(0, 1)),
                "BMI": str(truncated_gauss(15, 35, sigma=3)),
                "Age": str(truncated_gauss(1, 3, sigma=3)),
                "Education": str(truncated_gauss(1, 6, sigma=1)),
                "Income": str(truncated_gauss(1, 11, sigma=2)),
                "GenHlth": str(random.randint(1, 5)),
                "MentHlth": str(random.randint(0, 30)),
                "PhysHlth": str(random.randint(0, 30)),
                "EmailAddress": "".join(random.choice(string.ascii_letters) for _ in range(16)) + "@gmail.com"
            }
            volunteer = Volunteer(volunteer_dict)
            volunteer.predict()
            yield volunteer
