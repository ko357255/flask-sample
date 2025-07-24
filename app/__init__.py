from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy() #DB

# Flaskアプリを生成する関数
def create_app():
    
    # flaskアプリを作成
    app = Flask(__name__)

    # データベース設定
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sample.db' # DBのURL
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # SQLAlchemyの追跡をオフ

    # DBと連携
    db.init_app(app)
    
    # 循環参照してしまうので、関数の中でインポートを行う
    from app.routes.user import user_bp
    from app.routes.post import post_bp
    # ルートのブループリントの登録
    app.register_blueprint(user_bp)
    app.register_blueprint(post_bp)
    
    return app
    