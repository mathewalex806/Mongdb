from flask import Flask, render_template, url_for, request
from pymongo import MongoClient


app = Flask(__name__)

client = MongoClient()
db = client["flask-database"]
todos = db["todos"]


@app.route("/", methods=['GET','POST'])
def index():
    return render_template('index.html')




if __name__ == "__main__":
    app.run(debug=True)