# third party library
from flask import request, render_template

# local library
from application import app, db, STAGE_STRINGS
from application.models.volunteer import Volunteer
from application.services import volunteer_services
from application.tests.test_form import create_volunteers, delete_all_volunteers

@app.route("/", methods=["GET"])
def home():
    return render_template("home.html")


@app.route("/form", methods=["GET"])
def form():
    return render_template("form.html")


@app.route("/stage", methods=["GET", "POST"])
def stage():
    # 實例產生 (內含預測結果)
    volunteer = volunteer_services.create_volunteer(request.form)
    # 糖尿病階段
    stage = max(
        volunteer.Stage0_Reliabilities,
        volunteer.Stage1_Reliabilities,
        volunteer.Stage2_Reliabilities,
    )
    # 系統信心
    reliability = getattr(volunteer, f"Stage{stage}_Reliabilities")

    return render_template(
        "stage.html",
        reliability=reliability,
        stage_string_title=STAGE_STRINGS["title"][stage],
        stage_string_description=STAGE_STRINGS["description"][stage],
    )


@app.route("/dashboard", methods=["GET"])
def dashboard():
    """# NotImplemented"""
    # create_volunteers(10)
    delete_all_volunteers()

    # find_all
    volunteers = db.session.query(Volunteer).all()
    string_list = [str(volunteer.jsonify()) for volunteer in volunteers]

    return "<br>".join(string_list)
