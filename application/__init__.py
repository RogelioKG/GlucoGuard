# standard library
import os

# third party library
import joblib
import pandas as pd
from flask import Flask
from pathlib import Path
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy

##################################################
################## STAGE_STRINGS #################
##################################################

STAGE_STRINGS = pd.DataFrame(
    {
        "title": ["Stage 0: No Diabetes", "Stage 1: Prediabetes", "Stage 2: Diabetes"],
        "description": [
            "At this stage, individuals do not have diabetes. It is crucial to maintain a healthy lifestyle by engaging in regular physical activity, adopting a balanced diet rich in fruits, vegetables, and whole grains, and managing stress levels. Regular health check-ups are essential to monitor blood sugar levels and overall well-being. Stay proactive in making healthy choices to prevent the onset of diabetes.",
            "Prediabetes is a warning sign that blood sugar levels are higher than normal but not yet at the diabetes range. Focus on lifestyle modifications such as incorporating more physical activity into daily routines and making dietary changes. Choose complex carbohydrates, limit sugar intake, and opt for lean proteins. Weight management is key; even a modest weight loss can significantly reduce the risk of progressing to diabetes. Regular monitoring and consultation with healthcare professionals are vital to track progress and receive personalized guidance.",
            "Diabetes is a chronic condition where the body either does not produce enough insulin or cannot effectively use the insulin it produces. This results in elevated blood glucose levels. Symptoms of diabetes may include increased thirst, frequent urination, unexplained weight loss, fatigue, and blurred vision. However, some people with diabetes may not exhibit noticeable symptoms. Management of diabetes involves lifestyle modifications, including a well-balanced diet, regular exercise, monitoring blood glucose levels, and possibly medication or insulin therapy. Regular medical check-ups are crucial for monitoring and adjusting the treatment plan as needed.",
        ],
    }
)

##################################################
################ MODEL_PRETRAINED ################
##################################################

MODEL_PRETRAINED = joblib.load(Path.cwd() / "application/persistence_model/diabetes_prediction_model.pkl")

##################################################
####################### app ######################
##################################################

app = Flask(__name__)
load_dotenv()
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("SQLALCHEMY_DATABASE_URI")

##################################################
####################### db #######################
##################################################

db = SQLAlchemy(app)
# 這裡要引入 models，db 才會知道有哪些 table 要 create
from application.models import *
# 如果資料庫沒有 create table 的話，全部 create
with app.app_context():
    db.create_all()

##################################################
##################### (misc) #####################
##################################################

# app 註冊路由
from application.controllers import *
