# local library
from app import db


__all__ = [
    "volunteer"
]

class Jsonifiable:
    def jsonify():
        """轉為類 JSON 物件
        """
        raise NotImplementedError

class Generative: 
    @staticmethod
    def generate(n: int):
        """生成 n 筆隨機資料
        """
        raise NotImplementedError

class BaseDataModel(Jsonifiable, Generative):
    __tablename__: str
