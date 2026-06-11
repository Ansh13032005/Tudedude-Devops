from flask import Flask, jsonify, render_template, request
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient('mongodb://localhost:27017/')
db = client['todo_db']
collection = db['items']

@app.route('/api')
def api():
    return jsonify({"message": "Hello from Tutedude_new branch!", "status": "updated"})

@app.route('/todo')
def todo():
    return render_template('todo.html')

@app.route('/submittodoitem', methods=['POST'])
def submit_todo():
    item_name = request.form.get('itemName')
    item_desc = request.form.get('itemDescription')
    collection.insert_one({"itemName": item_name, "itemDescription": item_desc})
    return "Item Added Successfully!"

if __name__ == '__main__':
    app.run(debug=True)
