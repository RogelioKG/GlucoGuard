# Changelog

All notable changes to this project will be documented in this file.



## [Unreleased]

### Added
+ ...



## [0.2.1] - 2024-02-08

### Added
+ **Flask CLI** - 生成指令 `generate` 使用 tqdm 進度條

### Changed
+ **Flask CLI** - 生成 `generate` 獨立為一個指令，並使用選項 (如 `--volunteers`) 指定資料表
+ **Models** - 原先 _generate.py_ 中的 `random_form`，被整合至 `Volunteer` 的靜態方法 `generate`
+ **Models** - 新增 `Jsonifiable` / `Generative` / `BaseDataModel` 類別，要求之後所有資料表類別都應實作方法`jsonify` (每種資料應都能轉成 JSON 格式) 與 `generate` (每個資料表都有自己生成隨機資料的方法)



## [0.2.0] - 2024-02-07

### Added
+ **Flask CLI** - `flask db clear` (清空資料庫) & `flask db generate-volunteers 10` (生成 10 筆填表者 mock data)
+ **Unit Testing** - 單元測試

### Changed
+ **Flask Blueprint** - 重構 (refactor)，改用藍圖建構應用程式



## [0.1.0] - 2024-01-03

### Added
+ **Progress** : demo 完成



[unreleased]:#
[0.2.1]:#
[0.2.0]:#
[0.1.0]:#
