from app import db, ma
from sqlalchemy import Column, Integer, String


# モデルの定義
class User(db.Model):
    id = Column(Integer, primary_key=True)
    username = Column(String(100), nullable=False)
    
    def __str__(self):
        return self.username

    # # 辞書型に変換するメソッド (シリアライザを使わない場合)
    # def to_dict(self):
    #     return {
    #         "id": self.id,
    #         "username": self.username
    #     }

# JSONシリアライザとバリデーションを行う
# シリアライズ: モデルのインスタンスをJSONに変換する仕組み
class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        # デシリアライズ時(JSON→オブジェクト)、Userのインスタンスで返す
        load_instance = True

user_schema = UserSchema() # 単体オブジェクトのシリアライザ
users_schema = UserSchema(many=True) # 複数オブジェクトのシリアライザ