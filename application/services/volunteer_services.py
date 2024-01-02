# standard library
from typing import Any, Mapping

# third party library

# local library
from application import db, MODEL_PRETRAINED
from application.models.volunteer import Volunteer


def create_volunteer(form: Mapping[str, Any]) -> Volunteer:
    # 實例產生
    volunteer = Volunteer(**form)
    # 模型預測
    data = volunteer.standardize()
    result_proba = MODEL_PRETRAINED.predict_proba(data)

    # 資料庫操作
    try:
        (
            volunteer.Stage0_Reliabilities,
            volunteer.Stage1_Reliabilities,
            volunteer.Stage2_Reliabilities,
        ) = map(float, result_proba[0])
        db.session.add(volunteer)
        db.session.commit()
    # 異常回滾
    except Exception as err:
        db.session.rollback()
        
    return volunteer