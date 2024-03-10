# Required to reference other scripts
import sys
sys.path.append( '.' )
sys.path.append( '..' )

from flask import Flask, request, jsonify
from flask_cors import CORS
from ai_engine.chatbot import chat_with_user  # Import your chatbot logic here

app = Flask(__name__)
CORS(app)  # Enable CORS for AJAX requests

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("user_input")
    # response = chat_with_user(user_input)  # Adapt this to work with your chatbot logic
    response = chat_with_user()  # Adapt this to work with your chatbot logic
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
