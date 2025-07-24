from app import db

# モデルの定義
class User(db.Model):
    __tablename__ = 'users' # SQLのテーブル名
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    
    # １対多のリレーション
    posts = db.relationship('Post', backref='user', lazy=True, cascade='all, delete')
    # user.posts | post.user でアクセスが可能となる
    # cascade によりポストも同時に削除される
    
    def to_dict(self):
        return {"id": self.id, "username": self.username}

class Post(db.Model):
    __tablename__ = 'posts' # SQLのテーブル名
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    # 外部キー
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    
    def to_dict(self):
        return {"id": self.id, "title": self.title, "user_id": self.user_id}