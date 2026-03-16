from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Payment Service Running"

@app.route("/payments")
def payments():
    return {"payments": ["success","pending"]}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)