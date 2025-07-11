from flask import Flask, jsonify, request

app = Flask(__name__)

users = {}

@app.route('/')
def home():
    return "Welcome to the Flask API!"

@app.route('/data', methods=['GET'])
def data():
    return jsonify(list(users.keys()))

@app.route('/status', methods=['GET'])
def statue():
    return "OK"

@app.route('/users/<username>', methods=['GET'])
def get_user(username):
    user = users.get(username)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404


@app.route('/add_user', methods=['POST'])
def add_user():
    user = request.get_json()

    if not user or 'username' not in user:
        return jsonify({"error": "Username is required"}), 400

    username = user['username']
    users[username] = user
    return jsonify({
        "message": "User added",
        "user": user
    }), 201


if __name__ == "__main__":
    app.run()
