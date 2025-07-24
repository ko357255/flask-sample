from app import db

# モデルの定義
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    
    def to_dict(self):
        return {"id": self.id, "username": self.username}
    
    def __init__(self, username: str):
        self.username = username