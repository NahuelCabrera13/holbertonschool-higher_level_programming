from flask import Flask
from flask import jsonify
from flask import request

app = Flask(__name__)

users ={}

@app.route("/", methods=["GET"])
def home():
    return("Welcome to the Flask API!")

@app.route("/data", methods=["GET"])
def data():
    names = [user["name"] for user in users.values() if user.get("name")]
    return jsonify(names)

@app.route("/status")
def status():
    return "OK"

@app.route("/users/<usernames>")
def get_users(usernames):
    user = users.get(usernames)

    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404

@app.route('/add_user', methods=['POST'])
def add_user():
    user_data = request.get_json()
    print(user_data)

    if not user_data or "username" not in user_data or not user_data["username"]:
        return jsonify({"error": "Username is required"}), 400

    username = user_data["username"]

    users[username] = {
        "username": username,
        "name": user_data.get["name"],
        "age": user_data.get("age", 0),
        "city": user_data.get("city", "")
    }

    return jsonify({
        "message": "User added",
        "user": users[username]
    }), 201





if __name__ == "__main__":
    app.run(debug=True)
