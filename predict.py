import pickle
import re

model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

print("🔥 Script started")

def clean_text(text):
    text = text.lower()
    text = re.sub(r'\W', ' ', text)
    text = re.sub(r'\s+', ' ', text)
    return text

def predict_message(message):
    message = clean_text(message)
    vector = vectorizer.transform([message]).toarray()
    result = model.predict(vector)

    if result[0] == 1:
        return "⚠️ Spam / Phishing Detected"
    else:
        return "✅ Safe Message"

# 🔥 ADD THIS PART
print(predict_message("Congratulations! You won ₹5000 click now"))
print(predict_message("Hey bro let's meet tomorrow"))