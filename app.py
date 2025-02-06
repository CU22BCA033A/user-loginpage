from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Sample sensitive information
USERNAME = "admin"
PASSWORD = "Admin123"
API_KEY = "sample_api_key"
IP_ADDRESS = "192.168.1.1"

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    if data['username'] == USERNAME and data['password'] == PASSWORD:
        return jsonify({"message": "Login successful", "api_key": API_KEY, "ip_address": IP_ADDRESS})
    else:
        return jsonify({"message": "Invalid credentials"}), 401

if __name__ == '__main__':
    app.run(debug=True)