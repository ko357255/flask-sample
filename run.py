from app import create_app, db

# Flaskアプリの生成
app = create_app()

# DBの初期化  
with app.app_context():
    db.create_all()


# 実行
if __name__ == "__main__":
    app.run(port=5000, debug=True)