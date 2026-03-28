# app.py (Flask backend)
from flask import Flask, render_template, request, jsonify
from chatbot import get_response

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")   # templates/index.html now exists

@app.route("/get", methods=["POST"])
def chatbot_response():
    user_input = request.form.get("msg", "")
    print(f"Received from user: {user_input}")      # Debugging log
    response_text = get_response(user_input)
    print(f"Responding with: {response_text}")
    return jsonify({"response": response_text})

if __name__ == "__main__":
    app.run(debug=True)
