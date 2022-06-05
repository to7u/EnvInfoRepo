from flask import Flask
from flask import render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import pytz
from requests import post

# Flaskクラスのインスタンスを生成
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///practice.db'
db = SQLAlchemy(app)

"""
DB作成コマンド
ターミナル起動
pythonコマンド実行
対話モードにて以下コマンド実行(appの箇所は実行するスクリプト名を指定する)
from appimport db
db.create_all()
カレントに指定した名称のDBが生成されていれば問題ない
"""
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    body = db.Column(db.String(500), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now(pytz.timezone('Asia/Tokyo')))
 
@app.route('/')
def index():
    if request.method == 'GET':
        # クラスに対応したDBデータ全件取得
        posts = Post.query.all()
        # 第二引数へDBのデータを渡すことでHTMLテンプレートファイルへ引き渡せる
        # 受け渡す変数を定義しHTMLにて使用する
        return render_template('index.html', posts=posts)

# 許可するメソッドを記述
@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == "POST":
        title = request.form.get('title')
        body = request.form.get('body')
        # Postのインスタンスを作成
        post = Post(title=title, body=body)
        db.session.add(post)
        db.session.commit()
        return redirect('/')
    else:
        return render_template('create.html')

app.run(port=3000, host='0.0.0.0', debug=True)