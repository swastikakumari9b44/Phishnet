# 🛡️ PhishNet

### AI-Powered Phishing & Spam Detection API

PhishNet is a machine-learning powered security API that analyzes **messages, URLs, and screenshots** to identify potential phishing and spam threats.

It combines **NLP-based classification, TF-IDF feature extraction, heuristic analysis, URL inspection, and OCR** to generate a threat score, risk level, and explainable phishing indicators.

> **Detect suspicious content. Understand the risk. Identify the attack tactic.**

---

## 🚀 What PhishNet Does

PhishNet analyzes suspicious digital content through three complementary pipelines:

```text
                    ┌─────────────────────┐
                    │       PhishNet      │
                    │   Threat Analysis   │
                    └──────────┬──────────┘
                               │
              ┌────────────────┼────────────────┐
              │                │                │
              ▼                ▼                ▼
        📩 Text Analysis   🔗 URL Analysis   🖼️ Image Analysis
              │                │                │
              ▼                ▼                ▼
          TF-IDF + ML      URL Heuristics      OCR
              │                │                │
              └────────────────┼────────────────┘
                               ▼
                    ┌─────────────────────┐
                    │ Threat Assessment   │
                    ├─────────────────────┤
                    │ Prediction          │
                    │ Threat Score        │
                    │ Risk Level          │
                    │ Attack Tactics      │
                    │ Explanation         │
                    └─────────────────────┘
```

---

# ✨ Key Features

### 📩 1. Message & Text Analysis

**Endpoint:** `POST /analyze-text`

Analyzes SMS messages, emails, and other text content using:

* TF-IDF vectorization
* Machine-learning classification
* Phishing keyword detection
* Heuristic indicators
* Credential-request detection
* Urgency and financial-fraud indicators

The API returns a classification along with a threat score, risk level, detected tactics, and explanation.

---

### 🔗 2. Suspicious URL Detection

**Endpoint:** `POST /analyze-url`

Analyzes URLs for potentially malicious characteristics, including:

* Suspicious domain patterns
* Phishing-related keywords
* Fake login indicators
* Insecure HTTP connections
* Suspicious URL structures
* Potential impersonation patterns

---

### 🖼️ 3. Screenshot & Image Analysis

**Endpoint:** `POST /analyze-screenshot`

PhishNet can analyze screenshots of suspicious emails, messages, or web content.

The pipeline:

```text
Image
  ↓
Tesseract OCR
  ↓
Text Extraction
  ↓
PhishNet Analysis Pipeline
  ↓
Threat Assessment
```

This allows text-based phishing detection to be applied to content that is embedded inside an image.

---

### 🎯 4. Phishing Tactic Identification

Instead of returning only **Safe / Phishing**, PhishNet attempts to identify the type of social-engineering tactic detected.

Current indicators include:

| Tactic                   | Description                                                  |
| ------------------------ | ------------------------------------------------------------ |
| ⚡ Urgency                | Attempts to pressure the user into immediate action          |
| 🔐 Credential Harvesting | Requests for passwords, credentials, or account verification |
| 💳 Financial Fraud       | Suspicious banking, payment, or financial requests           |
| 🔗 Malicious Link        | Suspicious or potentially deceptive URLs                     |

---

### 📊 5. Threat Scoring

PhishNet generates a **0–100 threat score** and maps it to a risk category.

```text
0 ─────────────── 33 ─────────────── 66 ─────────────── 100
       LOW                 MEDIUM                 HIGH
```

The response can include:

* Threat score
* Risk level
* Prediction
* Detected issues
* Phishing tactics
* Explanation

---

# 🧠 Detection Pipeline

PhishNet uses different analysis strategies depending on the input.

### Text

```text
Input Message
      ↓
Text Preprocessing
      ↓
TF-IDF Vectorization
      ↓
ML Classification
      ↓
Heuristic Analysis
      ↓
Threat Scoring
      ↓
Risk + Tactics
```

### URL

```text
Input URL
    ↓
URL Parsing
    ↓
Pattern & Keyword Analysis
    ↓
Security / Structure Checks
    ↓
Threat Scoring
    ↓
Risk Assessment
```

### Screenshot

```text
Screenshot
    ↓
Tesseract OCR
    ↓
Extracted Text
    ↓
Text Analysis Pipeline
    ↓
Threat Assessment
```

---

# 🛠️ Tech Stack

| Category             | Technologies               |
| -------------------- | -------------------------- |
| **Language**         | Python 3.9+                |
| **Backend**          | Flask, Flask-CORS          |
| **Machine Learning** | scikit-learn, NumPy        |
| **NLP**              | TF-IDF Vectorization       |
| **OCR**              | Tesseract OCR, PyTesseract |
| **Image Processing** | Pillow (PIL)               |
| **Model Artifacts**  | Pickle                     |

---

# 📁 Project Structure

```text
PhishNet/
│
├── app.py                 # Flask API and route handlers
├── script.py              # Model training and TF-IDF vectorization
│
├── model.pkl              # Trained ML classification model
├── vectorizer.pkl         # Fitted TF-IDF vectorizer
│
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation
```

---

# 🚀 Getting Started

## Prerequisites

Make sure you have:

* Python 3.9+
* pip
* Tesseract OCR

### Install Tesseract

**Windows**

Download and install Tesseract OCR from the UB Mannheim distribution.

**Ubuntu / Debian**

```bash
sudo apt-get update
sudo apt-get install tesseract-ocr
```

**macOS**

```bash
brew install tesseract
```

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/swastikakumari9b44/Phishnet.git
cd Phishnet
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it:

**Windows**

```bash
venv\Scripts\activate
```

**macOS / Linux**

```bash
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🧠 Train the Model

The repository includes the trained model artifacts:

```text
model.pkl
vectorizer.pkl
```

If you want to retrain or regenerate them:

```bash
python script.py
```

---

## ▶️ Run the API

Start the Flask server:

```bash
python app.py
```

The API will be available at:

```text
http://127.0.0.1:8000
```

---

# 🧪 API Documentation

## 1. Analyze Text

### `POST /analyze-text`

**Content-Type**

```text
application/json
```

### Request

```json
{
  "message": "URGENT: Your bank account access has been suspended. Please verify your credentials immediately at http://login-secure-verify.com."
}
```

### Example Response

```json
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
```

---

## 2. Analyze URL

### `POST /analyze-url`

**Content-Type**

```text
application/json
```

### Request

```json
{
  "url": "http://verify-bank-login.com"
}
```

### Example Response

```json
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
```

---

## 3. Analyze Screenshot

### `POST /analyze-screenshot`

**Content-Type**

```text
multipart/form-data
```

### Request

Upload an image using the `file` field.

Supported formats:

```text
.png
.jpg
.jpeg
```

The image is processed using Tesseract OCR before the extracted text is passed through the phishing detection pipeline.

---

# 📸 Screenshots

> **Add your actual application screenshots here.**

### 🔍 Text Analysis

![PhishNet Text Analysis](screenshots/text-analysis.png)

### 🔗 URL Analysis

![PhishNet URL Analysis](screenshots/url-analysis.png)

### 🖼️ Screenshot Analysis

![PhishNet Screenshot Analysis](screenshots/screenshot-analysis.png)

### 📊 Threat Assessment

![PhishNet Threat Assessment](screenshots/threat-assessment.png)

---

# 📈 Model Evaluation

Add your **actual measured model performance** here.

For example:

| Metric    | Score |
| --------- | ----: |
| Accuracy  | `XX%` |
| Precision | `XX%` |
| Recall    | `XX%` |
| F1 Score  | `XX%` |

### Why this matters

Phishing detection is a classification problem where **false negatives can be particularly costly**. Therefore, precision and recall should be evaluated alongside accuracy.

> ⚠️ **Do not add estimated or manually calculated numbers. Use results from your actual test/evaluation dataset.**

---

# 🔐 Security Considerations

PhishNet is designed as a **threat-analysis prototype/API**, not as a replacement for production security infrastructure.

The current implementation relies on:

* Machine-learning classification
* Heuristic rules
* URL pattern analysis
* OCR
* Keyword and structural indicators

A production deployment would require additional safeguards such as:

* URL reputation services
* Domain intelligence
* Malware sandboxing
* Authentication and authorization
* Rate limiting
* Input validation
* Secure file handling
* Logging and monitoring
* Adversarial robustness testing

---

# 🔮 Future Improvements

Potential extensions include:

* [ ] Transformer-based NLP models
* [ ] More advanced URL reputation analysis
* [ ] Domain-age and WHOIS intelligence
* [ ] Threat-intelligence API integration
* [ ] Email header analysis
* [ ] Multilingual phishing detection
* [ ] Improved OCR preprocessing
* [ ] Model performance benchmarking
* [ ] Docker deployment
* [ ] Automated API testing
* [ ] CI/CD with GitHub Actions

---

# 💡 Why PhishNet?

Traditional phishing detection often relies heavily on static rules or blacklisted URLs.

PhishNet explores a hybrid approach:

```text
Machine Learning
       +
Heuristic Analysis
       +
URL Inspection
       +
OCR
       ↓
Explainable Threat Assessment
```

The goal is not simply to answer:

> **"Is this phishing?"**

but also:

> **"Why does this look suspicious?"**

and:

> **"What type of phishing tactic is being used?"**

---

# 👩‍💻 Author

### Swastika Kumari

AI/ML & Full-Stack Developer

* GitHub: https://github.com/swastikakumari9b44
* LinkedIn: **[Add your LinkedIn URL]**
* Email: **[Add your professional email]**

---

## ⭐ If you find this project interesting

Feel free to explore the repository, raise issues, or suggest improvements.

**Built with Python, Machine Learning, Flask, and OCR.**
