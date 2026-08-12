from flask import Flask, request, jsonify, send_from_directory
from network import Network
import os

# Finds the web-application folder
webFolder = os.path.join(os.path.dirname(__file__), "..", "web-application")

# Creates the Flask server
app = Flask(__name__)

# Creates one neural network that stays alive while the server is running
network = Network()

if os.path.exists("model.json"):
    network.load()

# Opens the web application
@app.route("/")
def home():
    return send_from_directory(webFolder, "index.html")

# Allows the HTML page to load CSS, JavaScript and other files
@app.route("/<path:filename>")
def webFiles(filename):
    return send_from_directory(webFolder, filename)

# Receives training data from JavaScript
@app.route("/train", methods=["POST"])
def train():
    data = request.get_json()

    if data is None:
        return jsonify({"error": "No data received"}), 400

    inputs = data.get("inputs")
    correctNumber = data.get("correctNumber")

    if not isinstance(inputs, list) or len(inputs) != 1600:
        return jsonify({"error": "Inputs must contain 1600 values"}), 400
    if not isinstance(correctNumber, int) or correctNumber < 0 or correctNumber > 9:
        return jsonify({"error": "Correct number must be between 0 and 9"}), 400

    loss, prediction  = network.train(inputs, correctNumber)
    network.save()

    return jsonify({
        "guess": prediction,
        "correctNumber": correctNumber,
        "loss": loss
    })

# Starts the server
if __name__ == "__main__":
    app.run(debug=True)