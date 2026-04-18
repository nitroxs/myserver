from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "server khdam"

# 👇 هنا ديرها
@app.route("/cmd")
def cmd():
    return {"cmd": "print('salam sahbi')"}

app.run(host="0.0.0.0", port=5000)