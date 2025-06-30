from flask import Flask, jsonify, request

app = Flask(__name__)

users = {}

@app.route('/')
def home():
    return "Welcome to the Flask API!"

@app.route('/data', methods=['GET'])
def data():
    return jsonify(list(users.keys()))

@app.route('/statue', methods=['GET'])
def statue():
    return "OK"

@app.route('/users/<username>', methods=['GET'])
def get_user(username):
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"})

@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.get_json()
    username = data.get('username')
    if not username or username in users:
        return jsonify({"error": "Username is required"})

    users[username] = {
        "name": data.get("name"),
        "age": data.get("age"),
        "city": data.get("city"),
    }

    return jsonify({
        "message": "User added successfully",
        "user": users[username]
    })




if __name__ == "__main__":
    app.run()