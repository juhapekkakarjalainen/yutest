from flask import Flask, request, jsonify
import aiml
kernel = aiml.Kernel()
kernel.learn("files/*.aiml")
app = Flask(__name__)

@app.route("/")
def home():
    return "Hippo chatbot toimii"

@app.route("/chat/<int:ika>")
def chat(ika):

    if ika <= 6:
        return "Voit osallistua 40 m, pituus ja pallonheitto."

    elif ika <= 8:
        return "Voit osallistua 40 m, pituus ja pallonheitto."

    elif ika <= 10:
        return "Voit osallistua 40 m, 1000 m, pituus ja kuula."

    elif ika <= 12:
        return "Voit osallistua 60 m, 1000 m, pituus ja kuula."

    elif ika <= 14:
        return "Voit osallistua 60 m, 200 m, korkeus ja pituus."

    else:
        return "Voit osallistua 100 m, 400 m, seiväs ja kuula."
