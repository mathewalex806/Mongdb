from flask import Flask, render_template, url_for, request
from pymongo import MongoClient


app = Flask(__name__)

client = MongoClient()
db = client["flask-database"]
todos = db["todos"]

list_item =[]

@app.route("/", methods=['GET','POST'])
def index():
    if request.method == 'POST':
        item = request.form["list_item"]

        if item not in list_item:
            insert_item = { "item": item,}
            todos.insert_one(insert_item)
            list_item.append(item)

        return render_template('index.html',list_items = todos.find())
    
    return render_template('index.html',list_items = todos.find())

if __name__ == "__main__":
    app.run(debug=True)