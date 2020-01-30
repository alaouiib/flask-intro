from flask import Flask, render_template, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_cors import CORS

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///Pytest.db"
db = SQLAlchemy(app)
tasks = [{"content": "task1",'date_created':datetime.today()}, {"content": "task2",'date_created':datetime.today()}]

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return "<Task %r>" % self.id


CORS(app)
@app.route("/")
def index():

    return render_template("index.html",tasks=tasks)


@app.route("/json/<int:id>", methods=["GET", "POST"])
def json(id):
    #     if request.method == 'POST':
    return jsonify({"key": id})


if __name__ == "__main__":
    app.run(debug=True)
