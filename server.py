from flask import Flask, request, jsonify

app = Flask(__name__)

users = {
    "admin": "1234"
}

@app.route("/")
def home():
    return "server khdam"

@app.route("/login", methods=["POST"])
def login():
    data = request.json
    if data["username"] in users and users[data["username"]] == data["password"]:
        return jsonify({"status": "ok"})
    return jsonify({"status": "error"})

@app.route("/run", methods=["POST"])
def run():
    data = request.json
    return jsonify({"result": f"khdam m3a {data['username']}"})

app.run()