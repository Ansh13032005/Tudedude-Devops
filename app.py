from flask import Flask, jsonify, render_template, request
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient('mongodb://localhost:27017/')
db = client['todo_db']
collection = db['items']

@app.route('/api')
def api():
    return jsonify({"message": "Hello from Tutedude_new branch!", "status": "updated"})

if __name__ == '__main__':
    app.run(debug=True)
