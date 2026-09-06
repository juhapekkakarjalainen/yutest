from flask import Flask, request, jsonify
import aiml

app = Flask(__name__)

kernel = aiml.Kernel()
kernel.learn("files/*.aiml")

@app.route("/")
def home():
    return "Yleisurheiluchatbot toimii"

@app.route("/chat", methods=["POST"])
def chat():
    message = request.json["message"]
    response = kernel.respond(message)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run()
