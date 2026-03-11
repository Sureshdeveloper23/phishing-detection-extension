from flask import Flask, request, jsonify, render_template
from model import predict_url

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h2>AI Phishing Detector</h2>
    <form method='POST' action='/check'>
        <input type='text' name='url' placeholder='Enter URL'>
        <button type='submit'>Check</button>
    </form>
    """

@app.route("/check", methods=["POST"])
def check():

    url = request.form["url"]
    result = predict_url(url)

    return f"<h3>Result: {result}</h3>"

@app.route("/predict", methods=["POST"])
def predict():

    data = request.json
    url = data["url"]

    result = predict_url(url)

    return jsonify({"result": result})

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000)
