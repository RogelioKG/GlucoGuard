# GlucoGuard v1.0
Last Update: 2024/1/3

![alt glucoguard](https://github.com/RogelioKG/GlucoGuard/blob/main/application/static/img/glucoguard-demo.gif?raw=true)

## Python Version
3.11.4

## Brief
填寫表單並透過持久化的預訓練模型，預測當前填表者的糖尿病階段，\
使用 PostgreSQL 儲存填表者資料，並使用 plotly 做為後臺實時資料可視化。

## Requirements
+ **flask**
+ **python-dotenv**
+ **psycopg2-binary**
+ **Flask-SQLAlchemy**
+ **pandas**
+ **xgboost**
+ **joblib**
+ **plotly**

## Setting up the Project
請參考 [TabulaTalent Backend](https://github.com/thewro11/tabula-talent-backend)，設置同此專案。
