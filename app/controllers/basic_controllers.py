# third party library
from flask import request, render_template
import pandas as pd

# local library
from . import basic_blueprint
from app import db
from app.constants import STAGE_STRINGS
from app.models.volunteer import Volunteer
from app.services import chart


# 首頁
@basic_blueprint.route("/", methods=["GET"])
def home():
    return render_template("home.html")


# 表單頁
@basic_blueprint.route("/form/", methods=["GET"])
def form():
    return render_template("form.html")


# 預測結果頁
@basic_blueprint.route("/stage/", methods=["GET", "POST"])
def stage():
    # 實例產生 (未含預測結果)
    volunteer = Volunteer(request.form)
    # 模型預測 (填入預測結果)
    volunteer.predict()
    # 資料庫操作
    db.session.add(volunteer)
    db.session.commit()
    # 系統信心
    reliabilities = [getattr(volunteer, column) for column in Volunteer.result_columns]
    # 最高系統信心
    reliability = max(reliabilities)
    # 糖尿病階段
    stage = reliabilities.index(reliability)

    return render_template(
        "stage.html",
        reliability=reliability,
        stage_string_title=STAGE_STRINGS["title"][stage],
        stage_string_description=STAGE_STRINGS["description"][stage],
    )


# 儀表板頁
@basic_blueprint.route("/dashboard/", methods=["GET"])
def dashboard():
    # 獲取所有填表者標準化 DataFrame
    volunteers = db.session.query(Volunteer).all()
    std_volunteers = [volunteer.standardize() for volunteer in volunteers]
    try:
        df = pd.concat(std_volunteers, ignore_index=True)
    except ValueError:
        df = pd.DataFrame(columns=[*Volunteer.data_columns, *Volunteer.other_columns, *Volunteer.result_columns])

    # 繪圖
    graphs = []
    for column in Volunteer.data_columns:
        graph = chart.count_bar_chart(df, column)
        if graph:
            graphs.append(graph)

    return render_template("dashboard.html", graphs=graphs)
