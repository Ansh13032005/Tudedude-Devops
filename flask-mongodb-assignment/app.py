from flask import Flask, jsonify, render_template, request, redirect, url_for
from pymongo import MongoClient
import json

app = Flask(__name__)

# MongoDB Atlas Connection
MONGO_URI = "mongodb://ansh132002:piaMEdyq40de4Gtk@alphacluster-shard-00-00.h1fav.mongodb.net:27017,alphacluster-shard-00-01.h1fav.mongodb.net:27017,alphacluster-shard-00-02.h1fav.mongodb.net:27017/Python?ssl=true&authSource=admin&retryWrites=true&w=majority"

client = MongoClient(MONGO_URI)

db = client["studentDB"]
collection = db["students"]


# Question 1 - API Route
@app.route('/api')
def get_api_data():

    with open('data.json', 'r') as file:
        data = json.load(file)

    return jsonify(data)


# Home Page
@app.route('/')
def home():
    return render_template('index.html')


# Question 2 - Submit Form
@app.route('/submit', methods=['POST'])
def submit():

    try:
        name = request.form['name']
        email = request.form['email']

        data = {
            "name": name,
            "email": email
        }

        collection.insert_one(data)

        return redirect(url_for('success'))

    except Exception as e:
        return render_template(
            'index.html',
            error=str(e)
        )


# Success Page
@app.route('/success')
def success():
    return render_template('success.html')


if __name__ == '__main__':
    app.run(debug=True)