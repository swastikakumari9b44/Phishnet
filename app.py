from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle
import re

app = Flask(__name__)
CORS(app)

# -------------------------
# LOAD MODEL
# -------------------------
model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

# -------------------------
# CLEAN TEXT
# -------------------------
def clean_text(text):
    text = text.lower()
    text = re.sub(r'\W', ' ', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

# -------------------------
# CORE ML ANALYSIS
# -------------------------
def analyze_ml(message):
    cleaned = clean_text(message)
    vector = vectorizer.transform([cleaned])

    result = model.predict(vector)[0]
    prob = model.predict_proba(vector)[0]

    # FIX: Use prob[1] (probability of class 1 = Phishing)
    phishing_prob = prob[1] if len(prob) > 1 else result
    score = int(phishing_prob * 100)

    # Cap score
    score = min(100, max(0, score))

    return result, score

# -------------------------
# DETECT TACTICS
# -------------------------
def detect_tactics(text):
    text_lower = text.lower()
    tactics = []

    if "urgent" in text_lower:
        tactics.append("Urgency")
    if "login" in text_lower or "verify" in text_lower:
        tactics.append("Credential Harvesting")
    if "click" in text_lower or "link" in text_lower:
        tactics.append("Malicious Link")
    if "bank" in text_lower or "account" in text_lower:
        tactics.append("Financial Fraud")
    if "otp" in text_lower or "password" in text_lower:
        tactics.append("Sensitive Data Request")

    return tactics

# -------------------------
# TEXT ANALYSIS
# -------------------------
@app.route("/analyze-text", methods=["POST"])
def analyze_text():
    data = request.get_json(silent=True) or {}
    message = data.get("message", "")

    if not message:
        return jsonify({"error": "No message provided"}), 400

    result, score = analyze_ml(message)

    # Keyword boosting (only boost if suspicious keywords are present)
    keywords = ["urgent", "verify", "login", "password", "otp", "bank", "click", "suspend"]
    if any(word in message.lower() for word in keywords):
        score = min(100, score + 15)

    # Risk logic
    if score > 75 or result == 1:
        risk = "High" if score > 75 else "Medium"
    elif score > 40:
        risk = "Medium"
    else:
        risk = "Low"

    tactics = detect_tactics(message)
    if not tactics and (result == 1 or score > 50):
        tactics = ["Suspicious Pattern"]

    return jsonify({
        "type": "Message",
        "prediction": "Phishing" if (result == 1 or score > 50) else "Safe",
        "score": score,
        "risk_level": risk,
        "tactics": tactics if tactics else ["None"],
        "explanation": "Detected phishing indicators such as suspicious keywords, urgency, or credential requests."
    })

# -------------------------
# URL ANALYSIS
# -------------------------
@app.route("/analyze-url", methods=["POST"])
def analyze_url():
    data = request.get_json(silent=True) or {}
    url = data.get("url", "").lower()

    if not url:
        return jsonify({"error": "No URL provided"}), 400

    result, score = analyze_ml(url)

    issues = []
    if "login" in url:
        issues.append("Fake Login Page")
    if "verify" in url:
        issues.append("Phishing Keyword")
    if url.startswith("http://"):
        issues.append("Not Secure (HTTP)")
    if "@" in url:
        issues.append("Suspicious URL Structure")
    if "-" in url:
        issues.append("Fake Domain Pattern")

    # Boost score if rule-based issues were found
    if issues:
        score = min(100, score + 20)

    # FIX: Combine ML model result AND heuristic issues for final prediction
    is_phishing = (result == 1) or len(issues) > 0 or score > 50

    if score > 75:
        risk = "High"
    elif score > 40:
        risk = "Medium"
    else:
        risk = "Low"

    return jsonify({
        "type": "URL",
        "prediction": "Phishing URL" if is_phishing else "Safe URL",
        "score": score,
        "risk_level": risk,
        "issues": issues,
        "explanation": "URL contains suspicious patterns such as fake login indicators or insecure structure."
    })

# -------------------------
# HOME
# -------------------------
@app.route("/")
def home():
    return "PhishNet API Running on Port 8000"

# -------------------------
# RUN SERVER
# -------------------------
if __name__ == "__main__":
    app.run(debug=True, port=8000)