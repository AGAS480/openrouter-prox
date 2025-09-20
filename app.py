from flask import Flask, request, jsonify
import requests, os

app = Flask(__name__)

# نقرأ التوكن الخاص بـ Wit.ai من متغير البيئة
WIT_TOKEN = os.environ.get("WIT_TOKEN")

@app.route("/parse")
def parse():
    q = request.args.get("q", "")
    if not q:
        return jsonify({"error": "no text provided"}), 400

    headers = {"Authorization": f"Bearer {WIT_TOKEN}"}
    params = {"v": "20230917", "q": q}

    r = requests.get("https://api.wit.ai/message", headers=headers, params=params)
    return jsonify(r.json())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
requests==2.31.0
gunicorn==21.2.0
