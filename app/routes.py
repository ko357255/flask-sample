from flask import jsonify, request, Blueprint
from app.models import User
from app import db

# ブループリントの生成
bp = Blueprint('user', __name__, url_prefix='/users') # /users.. から始まる

# ユーザー全件取得
@bp.route('/', methods=['GET'])
def get_users():
    users: list[User] = User.query.all()
    return jsonify([user.to_dict() for user in users])

# ユーザー追加
@bp.route('/', methods=['POST'])
def post_users():
    data = request.json # リクエストボディ
    user = User(username=data.get('username', ''))
    db.session.add(user)
    db.session.commit()
    return jsonify(user.to_dict()), 201

# ユーザー取得
@bp.route('/<int:id>', methods=['GET'])
def get_user(id):
    user = User.query.get_or_404(id)
    return jsonify(user.to_dict())
    

# ユーザー取得
@bp.route('/<int:id>', methods=['PUT'])
def update_user(id):
    user = User.query.get_or_404(id)
    
    data = request.json # リクエストボディ
    user.username = data.get('username', user.username)
    db.session.commit()
    return jsonify(user.to_dict())


# ヘルスチェック
@bp.route('/health', methods=['GET'])
def health():
    return jsonify(status="ok")
