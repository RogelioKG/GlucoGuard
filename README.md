# GlucoGuard
<!-- Badges -->
![Version 0.2.1](https://img.shields.io/badge/version-0.2.1-blue)
[![Python 3.11.4](https://img.shields.io/badge/python-3.11.4-blue)](https://www.python.org/downloads/release/python-3114/ "More details about Python 3.11.4")
![Last Updated](https://img.shields.io/badge/last%20updated-2024/2/6-darkgreen)
![Coverage](https://img.shields.io/badge/coverage-89%25-darkgreen)
[![Licence](https://img.shields.io/github/license/RogelioKG/GlucoGuard)](./LICENSE)



## Brief
填寫表單並透過持久化的預訓練模型，預測當前填表者的糖尿病階段，\
使用 PostgreSQL 儲存填表者資料，並使用 plotly 做為後臺實時資料可視化。
<!-- GIF -->
![glucoguard](./tests/demo/glucoguard-demo.gif?raw=true)


## Requirements

+ **flask**
+ **python-dotenv**
+ **psycopg2-binary**
+ **Flask-SQLAlchemy**
+ **pandas**
+ **xgboost**
+ **joblib**
+ **plotly**
+ **coverage**
+ **pytest**
+ **tqdm**


## Running the Flask Application
若你已設置好虛擬環境，並開啟 Docker 應用程式，你可以這樣運行此應用

> [!CAUTION]
> 由於存在第三方 JS 腳本 / CSS 樣式表，強烈建議連網運行，否則將導致功能或格式缺損

+ **Windows**

  + 本地運行
    ```bat
    scripts\dev_run.bat
    ```
  + Docker 容器運行
    ```bat
    scripts\docker_dev_run.bat
    ```


## Flask CLI
若為本地運行，可以使用以下命令列進行測試

  + 清空資料庫
    ```bat
    flask db clear
    ```
  + 生成 500 筆填表者 mock data
    ```bat
    flask db generate --volunteer 500
    ```


## Testing

  + 單元測試 (並產生 .coverage)
    ```bat
    scripts\test_run.bat
    ```
  + 覆蓋率報告 (需存在 .coverage)
    ```bat
    scripts\test_report.bat
    ```


## Changelog
> See notable changes to this project in [CHANGELOG.md](./CHANGELOG.md).
