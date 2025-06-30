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
    else:
        return jsonify({"error": "User not found"})

@app.route('/add_user', methods=['POST'])
def add_user():
    user = request.get_json()
    username = user.get('username')
    if not username:
        return jsonify({"error": "Username is required"})

    user_obj = {
        "username": username,
        "name": data.get("name"),
        "age": data.get("age"),
        "city": data.get("city")
    }
    users[username] = user_obj

    return jsonify({
        "message": "User added",
        "user": user_obj
    })




if __name__ == "__main__":
    app.run()