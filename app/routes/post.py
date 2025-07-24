from flask import jsonify, request, Blueprint
from app.models import Post
from app import db

# ブループリントの生成
post_bp = Blueprint('post', __name__, url_prefix='/posts') # /posts.. から始まる

# ポスト全件取得
@post_bp.route('', methods=['GET'])
def get_posts():
    posts: list[Post] = Post.query.all()
    return jsonify([post.to_dict() for post in posts])

# ポスト取得
@post_bp.route('/<int:id>', methods=['GET'])
def get_post(id):
    post = Post.query.get_or_404(id)
    return jsonify(post.to_dict())

# ポスト更新
@post_bp.route('/<int:id>', methods=['PUT'])
def update_post(id):
    post = Post.query.get_or_404(id)
    
    data = request.json # リクエストボディ
    post.title = data.get('title', post.title)
    db.session.commit()
    return jsonify(post.to_dict())

# ポスト編集
@post_bp.route('/<int:id>', methods=['DELETE'])
def delete_user(id):
    user = Post.query.get_or_404(id)
    db.session.delete(user)
    db.session.commit()
    return "", 200