from flask import Flask
from flask import jsonify
from flask import request

users ={
    "jane": {"username": "jane", "name": "Jane", "age": 28, "city": "Los Angeles"},
    "john": {"username": "john", "name": "John", "age": 30, "city": "New York"},
}

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return("Welcome to the Flask API!")

@app.route("/data", methods=["GET"])
def data():
    names = [data.get("name") for data in users.values() if "name" in data]
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
        return jsonify({"Error": "User not found"}), 404

@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.get_json()
    if not data or 'username' not in data:
        return jsonify({"error": "Username is required"}), 400
    username = data['username']

    users[username] = {
        "username": username,
        "name": data.get("name"),
        "age": data.get("age"),
        "city": data.get("city")
    }
    
    return jsonify({
        "message": "User  added",
        "user": users[username]
    }), 201



if __name__ == "__main__":
    app.run(debug=True)
