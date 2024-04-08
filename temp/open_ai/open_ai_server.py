from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Add this line to enable CORS for all routes

@app.route("/generate_text", methods=["POST"])
def generate_text():
    # Replace this with code to load and use your GPT-4 variant model
    prompt = request.json.get("prompt", "")
    generated_text = "This is a placeholder for generated text based on prompt: '{}'".format(prompt)
    return jsonify({"generated_text": generated_text})

if __name__ == "__main__":
    app.run(debug=True)
