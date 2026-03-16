from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Notification Service Running"

@app.route("/notify")
def notify():
    return {"status": "Notification sent"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5003)