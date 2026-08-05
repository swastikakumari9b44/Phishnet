🛡️ PhishNet: AI-Powered Phishing & Spam Detector
PhishNet is a real-time machine learning backend API designed to detect phishing attempts, suspicious URLs, and spam content across text messages and images. Built with Flask, scikit-learn, and OCR capabilities, PhishNet combines trained natural language processing models with heuristic rules to assign threat scores, risk levels, and specific attack tactics.

✨ Features
📩 Message Analysis (/analyze-text): Classifies SMS, emails, and plain text messages as Safe or Phishing using TF-IDF vectorization and machine learning, augmented by keyword heuristic boosting.

🔗 URL Analysis (/analyze-url): Detects malicious domain patterns, non-secure (HTTP) connections, and suspicious structure indicators.

🖼️ Screenshot / Image OCR (/analyze-screenshot): Uses Tesseract OCR to extract text from images/screenshots of suspicious emails or messages and evaluates them through the ML pipeline.

🎯 Threat Tactic Identification: Highlights specific phishing tactics, including Urgency, Credential Harvesting, Financial Fraud, and Malicious Links.

📊 Risk Scoring: Outputs a dynamic 0–100 threat score and categorized risk levels (Low, Medium, High).

🛠️ Tech Stack & Dependencies
Language: Python 3.9+

Framework: Flask, Flask-CORS

Machine Learning: scikit-learn, NumPy

OCR & Image Processing: Pillow (PIL), PyTesseract

📁 Project Structure
Plaintext
.
├── app.py                 # Main Flask API backend & route handlers
├── script.py              # ML model training and vectorization script
├── model.pkl              # Trained classification model
├── vectorizer.pkl         # Fitted TF-IDF Vectorizer
├── requirements.txt       # Project dependencies
└── README.md              # Project documentation
🚀 Getting Started
1. Prerequisites
Ensure you have Python installed on your machine. For image/screenshot analysis, install the Tesseract OCR Engine:

Windows: Download installer from UB-Mannheim/tesseract

Linux (Ubuntu/Debian): sudo apt-get install tesseract-ocr

macOS: brew install tesseract

2. Installation
Clone the repository and install the Python dependencies:

Bash
git clone https://github.com/your-username/phishnet.git
cd phishnet

pip install -r requirements.txt
3. Model Training (Optional)
If you need to retrain or regenerate the model artifacts (model.pkl and vectorizer.pkl):

Bash
python script.py
4. Running the API
Start the Flask server on [http://127.0.0.1:8000](http://127.0.0.1:8000):

Bash
python app.py
🧪 API Documentation & Endpoints
1. Analyze Text / Message
Endpoint: POST /analyze-text

Content-Type: application/json

Request Body:

JSON
{
  "message": "URGENT: Your bank account access has been suspended. Please verify your credentials immediately at http://login-secure-verify.com."
}
Response:

JSON
{
  "type": "Message",
  "prediction": "Phishing",
  "score": 90,
  "risk_level": "High",
  "tactics": [
    "Urgency",
    "Credential Harvesting",
    "Malicious Link",
    "Financial Fraud"
  ],
  "explanation": "Detected phishing indicators such as suspicious keywords, urgency, or credential requests."
}
2. Analyze URL
Endpoint: POST /analyze-url

Content-Type: application/json

Request Body:

JSON
{
  "url": "http://verify-bank-login.com"
}
Response:

JSON
{
  "type": "URL",
  "prediction": "Phishing URL",
  "score": 85,
  "risk_level": "High",
  "issues": [
    "Not Secure (HTTP)",
    "Fake Login Page",
    "Phishing Keyword",
    "Fake Domain Pattern"
  ],
  "explanation": "URL contains suspicious patterns such as fake login indicators or insecure structure."
}
3. Analyze Screenshot
Endpoint: POST /analyze-screenshot

Content-Type: multipart/form-data

Request Form Data:

file: [Upload image file (.png, .jpg, .jpeg)]
