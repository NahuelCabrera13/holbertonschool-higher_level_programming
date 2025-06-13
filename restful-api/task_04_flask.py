from flask import Flask, request, jsonify

app = Flask(__name__)

usuarios = {} 
@app.route('/')
def home():
    return 'Welcome to the User API!', 200

@app.route('/data', methods=['GET'])
def data():
    return jsonify(list(usuarios.values())), 200

@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.get_json()

    if not data or 'username' not in data:
        return jsonify({'error': 'Username is required'}), 400

    username = data['username']

    if username in usuarios:
        return jsonify({'error': 'Username already exists'}), 400

    usuarios[username] = data
    return jsonify({'message': 'User added successfully'}), 201

@app.route('/users/<username>', methods=['GET'])
def get_user(username):
    if username in usuarios:
        return jsonify(usuarios[username]), 200
    else:
        return jsonify({'error': 'User not found'}), 404

@app.route('/status', methods=['GET'])
def status():
    return jsonify({'status': 'OK'}), 200

if __name__ == '__main__':
    app.run(debug=True)