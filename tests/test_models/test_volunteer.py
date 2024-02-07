# standard libraray
import datetime

# third party library
import pytest

# local library
from app.models.volunteer import Volunteer


class TestVolunteer:

    def test_new_volunteer(self, new_volunteer: Volunteer):
        assert new_volunteer.buildDate == datetime.datetime.utcfromtimestamp(
            1704013390989 / 1000
        )  # 1704013390989 is unix time (ms)
        assert new_volunteer.HighBP == 1
        assert new_volunteer.HighChol == 1
        assert new_volunteer.CholCheck == 0
        assert new_volunteer.Smoker == 0
        assert new_volunteer.Stroke == 1
        assert new_volunteer.HeartDiseaseorAttack == 0
        assert new_volunteer.PhysActivity == 1
        assert new_volunteer.Fruits == 0
        assert new_volunteer.Veggies == 1
        assert new_volunteer.HvyAlcoholConsump == 0
        assert new_volunteer.AnyHealthcare == 1
        assert new_volunteer.NoDocbcCost == 0
        assert new_volunteer.DiffWalk == 1
        assert new_volunteer.Sex == 0
        assert new_volunteer.BMI == 30
        assert new_volunteer.Age == 40
        assert new_volunteer.Education == 6
        assert new_volunteer.Income == 11
        assert new_volunteer.GenHlth == 3
        assert new_volunteer.MentHlth == 20
        assert new_volunteer.PhysHlth == 12
        assert new_volunteer.EmailAddress == "testvolunteer@gmail.com"
        # 欄位預設就是 None，不管你有沒有設定屬性
        assert new_volunteer.Stage0_Reliabilities is None
        assert new_volunteer.Stage1_Reliabilities is None
        assert new_volunteer.Stage2_Reliabilities is None

    def test_jsonify(self, new_volunteer: Volunteer):

        volunteer_dict = new_volunteer.jsonify()

        assert volunteer_dict["buildDate"] == datetime.datetime.utcfromtimestamp(
            1704013390989 / 1000
        )  # unixtime (ms)
        assert volunteer_dict["HighBP"] == 1
        assert volunteer_dict["HighChol"] == 1
        assert volunteer_dict["CholCheck"] == 0
        assert volunteer_dict["Smoker"] == 0
        assert volunteer_dict["Stroke"] == 1
        assert volunteer_dict["HeartDiseaseorAttack"] == 0
        assert volunteer_dict["PhysActivity"] == 1
        assert volunteer_dict["Fruits"] == 0
        assert volunteer_dict["Veggies"] == 1
        assert volunteer_dict["HvyAlcoholConsump"] == 0
        assert volunteer_dict["AnyHealthcare"] == 1
        assert volunteer_dict["NoDocbcCost"] == 0
        assert volunteer_dict["DiffWalk"] == 1
        assert volunteer_dict["Sex"] == 0
        assert volunteer_dict["BMI"] == 30
        assert volunteer_dict["Age"] == 40
        assert volunteer_dict["Education"] == 6
        assert volunteer_dict["Income"] == 11
        assert volunteer_dict["GenHlth"] == 3
        assert volunteer_dict["MentHlth"] == 20
        assert volunteer_dict["PhysHlth"] == 12
        assert volunteer_dict["EmailAddress"] == "testvolunteer@gmail.com"
        assert new_volunteer.Stage0_Reliabilities is None
        assert new_volunteer.Stage1_Reliabilities is None
        assert new_volunteer.Stage2_Reliabilities is None

    def test_standardize(self, new_volunteer: Volunteer):
        data = new_volunteer.standardize()

        for column in Volunteer.other_columns:
            with pytest.raises(KeyError):
                data[column]

        for column in Volunteer.result_columns:
            with pytest.raises(KeyError):
                data[column]

    def test_predict(self, new_volunteer: Volunteer):
        new_volunteer.predict()
        for column in Volunteer.result_columns:
            assert 0 <= getattr(new_volunteer, column) <= 1
