# third party library
from flask import request, render_template

# local library
from application import app, db, STAGE_STRINGS, MODEL_PRETRAINED
from application.models.volunteer import Volunteer


@app.route("/", methods=["GET"])
def home():
    return render_template("home.html")


@app.route("/form", methods=["GET"])
def form():
    return render_template("form.html")


@app.route("/stage", methods=["GET", "POST"])
def stage():
    volunteer = Volunteer(**request.form)

    # 模型預測
    data = volunteer.standardize()
    result = MODEL_PRETRAINED.predict(data)
    result_proba = MODEL_PRETRAINED.predict_proba(data)
    stage = result[0]

    # 資料庫操作
    (
        volunteer.Stage0_Reliabilities,
        volunteer.Stage1_Reliabilities,
        volunteer.Stage2_Reliabilities,
    ) = map(float, result_proba[0])
    db.session.add(volunteer)
    db.session.commit()

    return render_template(
        "stage.html",
        reliability=result_proba[0][stage],
        stage_string_title=STAGE_STRINGS["title"][stage],
        stage_string_description=STAGE_STRINGS["description"][stage],
    )


@app.route("/dashboard", methods=["GET"])
def dashboard():
    """ # NotImplemented
    """
    volunteers = db.session.query(Volunteer).all()
    print(len(volunteers))
    string_list = [str(volunteer.jsonify()) for volunteer in volunteers]
    return "<br>".join(string_list)
