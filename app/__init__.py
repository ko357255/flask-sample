from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow


# flaskアプリを作成
app = Flask(__name__)

# データベース設定
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sample.db' # DBのURL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # SQLAlchemyの追跡をオフ

db = SQLAlchemy(app) #DB
ma = Marshmallow(app) #シリアライザ

with app.app_context():
    print('initiaze')
    db.create_all() # DBの初期化