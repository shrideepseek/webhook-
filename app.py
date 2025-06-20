import os
from flask import Flask, request
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

VERIFY_TOKEN = os.getenv("VERIFY_TOKEN")

@app.route("/webhook", methods=["GET", "POST"])
def webhook():
    if request.method == "GET":
        # WhatsApp webhook verification
        token = request.args.get("hub.verify_token")
        challenge = request.args.get("hub.challenge")
        if token == VERIFY_TOKEN:
            return challenge
        return "Verification token mismatch", 403

    if request.method == "POST":
        # Handles WhatsApp messages
        data = request.get_json()
        print("Received WhatsApp data:", data)
        return "EVENT_RECEIVED", 200

    return "Method Not Allowed", 405

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
