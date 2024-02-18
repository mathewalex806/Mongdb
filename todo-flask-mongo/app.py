from flask import Flask, render_template, url_for, request
from pymongo import MongoClient
from bson.objectid import ObjectId


app = Flask(__name__)

client = MongoClient()
db = client["flask-database"]
todos = db["todos"]

list_item =['updated_value']  

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



@app.route("/update", methods = ['POST','GET'])
def update():
    if request.method == 'POST':
        item_id = request.form["id"]
        db.todos.update_one({'_id': ObjectId(f"{item_id}")},  {'$set': {"item": "updated_value"}}) 
        return render_template('index.html', list_items = todos.find())

    else:
        return render_template('index.html',list_items = todos.find())
   


@app.route("/delete" , methods = ['GET','POST'])
def delete():
     if request.method == 'POST':
          item_id = request.form["id"]
          db.todos.delete_one({"_id":ObjectId(f"{item_id}")})
          print(item_id)
          return render_template('index.html', list_items = todos.find())
     return render_template('index.html', list_items = todos.find())




if __name__ == "__main__":
    app.run(debug=True)