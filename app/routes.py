from flask import jsonify, request
from app import app, db
from app.models import User, user_schema, users_schema

# エンドポイント

# バックエンドのヘルスチェック
@app.route("/health", methods=["GET"])
def health_check():
    return jsonify(status="ok"), 200


# ユーザー全件取得
@app.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    
    return users_schema.jsonify(users)
    # return jsonify([user.to_dict() for user in users]) # シリアライザを使わない場合

# ユーザー追加
@app.route('/users', methods=['POST'])
def post_users():
    data = request.json # リクエストボディ
    new_user = user_schema.load(data)
    # new_user = User(username=data['username']) # シリアライザを使わない場合
    
    db.session.add(new_user)
    db.session.commit()
    
    return user_schema.jsonify(new_user), 201

# ユーザー取得
@app.route('/users/<int:id>', methods=['GET'])
def get_user(id):
    user = User.query.get(id)
    if user:
        return user_schema.jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404

# ユーザー取得
@app.route('/users/<int:id>', methods=['PUT'])
def update_user(id):
    user = User.query.get(id)
    if user is None:
        return jsonify({"error": "User not found"}), 404
    
    data = request.json # リクエストボディ
    user.username = data['username']
    db.session.commit()
    return user_schema.jsonify(user)