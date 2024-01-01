# standard library
from typing import Any
import datetime

# third party library
from sqlalchemy import Column, Integer, Text, DateTime, Float, UUID
import pandas as pd
import uuid

# local library
from application import db

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
    Stage0_Reliabilities = Column(Float(8))
    Stage1_Reliabilities = Column(Float(8))
    Stage2_Reliabilities = Column(Float(8))

    other_columns = tuple([
        "id",
        "buildDate", 
        "EmailAddress"
    ])

    data_columns = tuple([
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
    ])

    result_columns = tuple([
        "Stage0_Reliabilities",
        "Stage1_Reliabilities",
        "Stage2_Reliabilities"
    ])

    def __init__(self, **kwargs: Any) -> None:
        """填表單者 database table
        
        僅將存在於 `Volunteer.data_columns` 與 `Volunteer.other_columns` 的 kw 設為 attribute
        
        並將預測結果賦值給 `volunteer_instance.Reliabilities`，其應為有 3 個元素的 `list[float]`
        
        以上皆完成後才能將這筆資料存入資料庫
        """
        for column in Volunteer.data_columns:
            if column == "BMI":
                setattr(self, column, float(kwargs[column]))
            else:
                setattr(self, column, int(kwargs[column]))
        for column in Volunteer.other_columns:
            if column == "id":
                setattr(self, column, kwargs[column])
            elif column == "buildDate":
                setattr(self, column, datetime.datetime.utcfromtimestamp(float(kwargs[column]) / 1000))
            else:
                setattr(self, column, str(kwargs[column])) 

    def jsonify(self) -> dict[str, Any]:
        """轉為 JSON 格式

        Returns
        -------
        (dict[str, Any])
        """
        volunteer_dict = dict()
        for column in Volunteer.data_columns:
            volunteer_dict[column] = getattr(self, column)
        for column in Volunteer.other_columns:
            volunteer_dict[column] = getattr(self, column)
        for column in Volunteer.result_columns:
            try:
                volunteer_dict[column] = getattr(self, column)
            except AttributeError:
                volunteer_dict[column] = None
        return volunteer_dict
    
    def standardize(self) -> pd.DataFrame:
        """產生可直接丟入模型 predict 的資料

        Returns
        -------
        (pd.DataFrame)
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

    
        # 表單範例
        # ImmutableDict(
        #     [
        #         ("formID", "233635142103444"),
        #         (
        #             "jsExecutionTracker",
        #             "build-date-1704013390989=>init-started:1704018466372=>validator-called:1704018466378=>validator-mounted-true:1704018466378=>init-complete:1704018466381=>interval-complete:1704018487387=>onsubmit-fired:1704018492697=>submit-validation-passed:1704018492700",
        #         ),
        #         ("submitSource", "form"),
        #         ("buildDate", "1704013390989"),  # --> unixtime ms version
        #         ("HighBP", "1"),
        #         ("HighChol", "1"),
        #         ("CholCheck", "0"),
        #         ("Smoker", "0"),
        #         ("Stroke", "1"),
        #         ("HeartDiseaseorAttack", "0"),
        #         ("PhysActivity", "1"),
        #         ("Fruits", "0"),
        #         ("Veggies", "1"),
        #         ("HvyAlcoholConsump", "0"),
        #         ("AnyHealthcare", "1"),
        #         ("NoDocbcCost", "0"),
        #         ("DiffWalk", "1"),
        #         ("Sex", "0"),
        #         ("BMI", "123"),
        #         ("Age", "11"),
        #         ("Education", "6"),
        #         ("Income", "11"),
        #         ("GenHlth", "3"),
        #         ("MentHlth", "20"),
        #         ("PhysHlth", "12"),
        #         ("EmailAddress", "t126017977@gmail.com"),
        #         ("formOpenId_V5", "14999403757376451606"),
        #         ("timeToSubmit", "20"),
        #         ("event_id", "1704018466380_233635142103444_9Ev2l4U"),
        #         ("validatedNewRequiredFieldIDs", '{"new":1}'),
        #     ]
        # )