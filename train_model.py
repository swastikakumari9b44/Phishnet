import pandas as pd
import numpy as np
import re
import pickle

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

# -------------------------------
# STEP 1: LOAD DATASET
# -------------------------------
# Try both formats (CSV or raw text file)

try:
    df = pd.read_csv("spam.csv", encoding='latin-1')
    df = df[['v1', 'v2']]
    df.columns = ['label', 'text']
except:
    # If dataset is in raw format (SMSSpamCollection)
    df = pd.read_csv("SMSSpamCollection", sep='\t', header=None)
    df.columns = ['label', 'text']

# -------------------------------
# STEP 2: CONVERT LABELS
# -------------------------------
df['label'] = df['label'].map({'ham': 0, 'spam': 1})

# -------------------------------
# STEP 3: CLEAN TEXT
# -------------------------------
def clean_text(text):
    text = text.lower()
    text = re.sub(r'\W', ' ', text)
    text = re.sub(r'\s+', ' ', text)
    return text

df['text'] = df['text'].apply(clean_text)

# -------------------------------
# STEP 4: TF-IDF VECTORIZATION
# -------------------------------
vectorizer = TfidfVectorizer(
    stop_words='english',
    ngram_range=(1,2),
    max_features=5000,
    min_df=2
)
X = vectorizer.fit_transform(df['text']).toarray()
y = df['label']

# -------------------------------
# STEP 5: TRAIN-TEST SPLIT
# -------------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# -------------------------------
# STEP 6: TRAIN MODEL
# -------------------------------
model = MultinomialNB()
model.fit(X_train, y_train)

# -------------------------------
# STEP 7: EVALUATE
# -------------------------------
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

print("✅ Model trained successfully")
print(f"🎯 Accuracy: {accuracy * 100:.2f}%")

# -------------------------------
# STEP 8: SAVE MODEL (IMPORTANT)
# -------------------------------
pickle.dump(model, open("model.pkl", "wb"))
pickle.dump(vectorizer, open("vectorizer.pkl", "wb"))

print("💾 Model and vectorizer saved as model.pkl & vectorizer.pkl")