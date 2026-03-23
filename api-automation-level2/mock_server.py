from flask import Flask, request, jsonify

app = Flask(__name__)

# -------- AUTH --------
@app.route('/auth/login', methods=['POST'])
def login():
    data = request.json

    if not data or not data.get("email") or not data.get("password"):
        return jsonify({"error": "Invalid input"}), 400

    if data["email"] == "admin@test.com" and data["password"] == "password":
        return jsonify({"access_token": "token123"}), 200

    return jsonify({"error": "Unauthorized"}), 401


# -------- USERS --------
@app.route('/users', methods=['GET', 'POST'])
def users():
    if request.method == 'GET':
        return jsonify([{"id": 1, "email": "test@test.com"}]), 200

    if request.method == 'POST':
        return jsonify({"id": 2}), 201


# -------- PROJECTS --------
@app.route('/projects', methods=['POST'])
def projects():
    return jsonify({"id": 1, "name": "Demo Project"}), 201


# -------- TASKS --------
@app.route('/tasks', methods=['POST'])
def tasks():
    return jsonify({"id": 1, "title": "Task"}), 201


# -------- COMMENTS --------
@app.route('/comments', methods=['POST'])
def comments():
    return jsonify({"id": 1, "message": "Done"}), 201


# -------- API LAB --------
@app.route('/api/lab/status/<int:code>', methods=['GET'])
def status(code):
    return jsonify({"status": code}), code


# -------- ANALYTICS --------
@app.route('/analytics', methods=['GET'])
def analytics():
    return jsonify({"users": 5, "projects": 2}), 200


if __name__ == "__main__":
    app.run(port=5000)