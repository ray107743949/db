from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///election.db'
db = SQLAlchemy(app)

class Election(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    date = db.Column(db.Date, nullable=False)
    location = db.Column(db.String(255), nullable=False)

class Candidate(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    party = db.Column(db.String(255), nullable=False)
    election_id = db.Column(db.Integer, db.ForeignKey('election.id'), nullable=False)

class Voter(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    id_card = db.Column(db.String(20), nullable=False, unique=True)
    address = db.Column(db.String(255), nullable=False)

# 路由部分
@app.route('/')
def index():
    elections = Election.query.all()
    return render_template('index.html', elections=elections)

# 其他路由部分，包括新增、查詢、更新、刪除候選人、選民等，請根據需要進行擴展。

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
