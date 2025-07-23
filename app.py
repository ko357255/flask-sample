from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

# flaskアプリを作成
app = Flask(__name__)

# データベース設定
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sample.db' # DBのURL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # SQLAlchemyの追跡をオフ

db = SQLAlchemy(app) #DB

# モデルの定義
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    
    def to_dict(self):
        return {"id": self.id, "username": self.username}

# DBの初期化  
with app.app_context():
    db.create_all()

# ユーザー全件取得
@app.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([user.to_dict() for user in users])

# ユーザー追加
@app.route('/users', methods=['POST'])
def post_users():
    data = request.json # リクエストボディ
    user = User(username=data.get('username', ''))
    db.session.add(user)
    db.session.commit()
    return jsonify(user.to_dict()), 201

# ユーザー取得
@app.route('/users/<int:id>', methods=['GET'])
def get_user(id):
    user = User.query.get_or_404(id)
    return jsonify(user.to_dict())
    

# ユーザー取得
@app.route('/users/<int:id>', methods=['PUT'])
def update_user(id):
    user = User.query.get_or_404(id)
    
    data = request.json # リクエストボディ
    user.username = data.get('username', user.username)
    db.session.commit()
    return jsonify(user.to_dict())


# ヘルスチェック
@app.route('/health', methods=['GET'])
def health():
    return jsonify(status="ok")


# 実行
if __name__ == "__main__":
    app.run(port=5000, debug=True)