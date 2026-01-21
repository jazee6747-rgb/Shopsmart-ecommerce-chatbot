from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def chatbot_response(message):
    message = message.lower()

    if "product" in message:
        return "We sell mobiles, laptops, headphones, and accessories."
    elif "price" in message:
        return "Prices start from ₹999 depending on the product."
    elif "delivery" in message:
        return "Delivery takes 3–5 business days."
    elif "return" in message:
        return "You can return products within 7 days."
    elif "payment" in message:
        return "We accept UPI, Credit Card, Debit Card, and Cash on Delivery."
    else:
        return "Sorry, I can answer only e-commerce related questions."

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json["message"]
    reply = chatbot_response(user_message)
    return jsonify({"reply": reply})

@app.route("/")
def home():
    return "E-commerce chatbot backend running"

  if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
