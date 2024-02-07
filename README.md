# GlucoGuard
<!-- Badges -->
![Version 0.2.0](https://img.shields.io/badge/version-0.2.0-blue)
[![Python 3.11.4](https://img.shields.io/badge/python-3.11.4-blue)](https://www.python.org/downloads/release/python-3114/ "More details about Python 3.11.4")
![Last Update](https://img.shields.io/badge/last%20update-2024/2/6-darkgreen)
![Coverage](https://img.shields.io/badge/coverage-88%25-darkgreen)
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


## Running the Flask Application
若你已設置好虛擬環境，並開啟 Docker 應用程式，你可以這樣運行此應用

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
  + 生成 10 筆填表者 mock data
    ```bat
    flask db generate-volunteers 10
    ```

## Testing

  + 單元測試 <span style="color: gray;">**(#todo)**</span>
    ```bat
    scripts\test_run.bat
    ```

## Change Log
> You can see more notable changes to this project in [CHANGELOG.md](./CHANGELOG.md).
