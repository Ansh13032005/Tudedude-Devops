from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app) # Enable CORS for frontend communication

@app.route('/process', methods=['POST'])
def process():
    data = request.json
    if not data or 'name' not in data:
        return jsonify({"error": "Name is required"}), 400
        
    return jsonify({"message": f"Hello {data['name']}! Data received successfully."})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
