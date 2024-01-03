# third party library
from flask import request, render_template

# local library
from application import app, STAGE_STRINGS
from application.models.volunteer import Volunteer
from application.services import volunteer_services, dashboard_services
from application.tests.generate import random_form


# 首頁
@app.route("/", methods=["GET"])
def home():
    return render_template("home.html")


# 表單頁
@app.route("/form", methods=["GET"])
def form():
    return render_template("form.html")


# 預測結果頁
@app.route("/stage", methods=["GET", "POST"])
def stage():
    # 實例產生 (內含預測結果)
    volunteer = volunteer_services.create_volunteer(request.form)

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
@app.route("/dashboard", methods=["GET"])
def dashboard():

    # 新增隨機資料
    for _ in range(50):
        volunteer_services.create_volunteer(random_form())

    # 刪除所有資料
    # volunteer_services.delete_all_volunteers()

    # 繪圖
    graphs = []
    for column in Volunteer.data_columns:
        graph = dashboard_services.count_bar_chart(column)
        if graph:
            graphs.append(graph)

    return render_template(
        "dashboard.html", 
        graphs=graphs
    )
