from flask import jsonify, request, Blueprint
from app.models import User, Post
from app import db

# ブループリントの生成
user_bp = Blueprint('user', __name__, url_prefix='/users') # /users.. から始まる

# ユーザー全件取得
@user_bp.route('', methods=['GET'])
def get_users():
    users: list[User] = User.query.all()
    return jsonify([user.to_dict() for user in users])

# ユーザー追加
@user_bp.route('', methods=['POST'])
def create_user():
    data = request.json # リクエストボディ
    user = User(username=data.get('username', ''))
    db.session.add(user)
    db.session.commit()
    return jsonify(user.to_dict()), 201

# ユーザー取得
@user_bp.route('/<int:id>', methods=['GET'])
def get_user(id):
    user = User.query.get_or_404(id)
    return jsonify(user.to_dict())

# ユーザー更新
@user_bp.route('/<int:id>', methods=['PUT'])
def update_user(id):
    user = User.query.get_or_404(id)
    
    data = request.json # リクエストボディ
    user.username = data.get('username', user.username)
    db.session.commit()
    return jsonify(user.to_dict())

# ユーザー削除
@user_bp.route('/<int:id>', methods=['DELETE'])
def delete_user(id):
    user = User.query.get_or_404(id)
    db.session.delete(user)
    db.session.commit()
    return "", 200

### ポスト

# ポスト投稿
@user_bp.route('/<int:id>/posts', methods=['POST'])
def create_user_posts(id):
    user = User.query.get_or_404(id)
    
    data = request.json # リクエストボディ
    post = Post(title=data.get('title', ''), user_id=user.id) # user_idを指定
    db.session.add(post)
    db.session.commit()
    
    return jsonify(post.to_dict()), 201

# ポスト一覧取得
@user_bp.route('/<int:id>/posts', methods=['GET'])
def get_user_posts(id):
    user = User.query.get_or_404(id)
    
    # リレーションの posts から取得
    posts: list[Post] = user.posts
    return jsonify([post.to_dict() for post in posts])
    