from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"message": "Hello from the custom Anki Sync Server!"})

@app.route("/healthz")
def health():
    return "ok", 200

if __name__ == "__main__":
    # Run on localhost:8080 by default
    app.run(host="0.0.0.0", port=8080)

