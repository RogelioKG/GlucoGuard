# standard library
from typing import Any, Mapping

# local library
from application import db, MODEL_PRETRAINED
from application.models.volunteer import Volunteer


def create_volunteer(form: Mapping[str, Any]) -> Volunteer:
    """創建填表者，並預測糖尿病階段，填入資料庫

    Parameters
    ----------
    + `form` (Mapping[str, Any]) : 表單

    Returns
    -------
    + `volunteer` (Volunteer) : 填表者
    """
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


def get_all_volunteers() -> list[Volunteer]:
    """取得所有填表者

    Returns
    -------
    + `volunteers` (list[Volunteer]) : 所有填表者
    """
    volunteers = db.session.query(Volunteer).all()
    return volunteers


def delete_all_volunteers() -> None:
    """刪除所有填表者
    """
    try:
        db.session.query(Volunteer).delete()
        db.session.commit()
    except Exception as err:
        db.session.rollback()
