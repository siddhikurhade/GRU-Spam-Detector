from flask import Flask, render_template, request
import tensorflow as tf
import pickle
import re
import numpy as np
from tensorflow.keras.preprocessing.sequence import pad_sequences

app = Flask(__name__)

# =========================
# LOAD MODEL
# =========================

model = tf.keras.models.load_model("GRU_Spam_Detector.h5")

# =========================
# LOAD TOKENIZER
# =========================

with open("GRU_Tokenizer.pkl", "rb") as f:
    tokenizer = pickle.load(f)

# =========================
# SETTINGS
# =========================

MAX_LEN = 100
THRESHOLD = 0.2

# =========================
# CLEAN TEXT FUNCTION
# =========================

def clean_text(text):

    text = text.lower()

    # Remove URLs
    text = re.sub(r"http\S+", "", text)

    # Remove special characters
    text = re.sub(r"[^a-zA-Z0-9\s]", "", text)

    # Remove extra spaces
    text = re.sub(r"\s+", " ", text).strip()

    return text

# =========================
# HOME ROUTE
# =========================

@app.route("/", methods=["GET", "POST"])
def index():

    prediction = None
    confidence = None
    raw_score = None
    user_input = ""

    if request.method == "POST":

        # Get message
        user_input = request.form["message"]

        # Clean message
        cleaned_text = clean_text(user_input)

        print("\n======================")
        print("Original Text:", user_input)
        print("Cleaned Text:", cleaned_text)

        # Convert to sequence
        sequence = tokenizer.texts_to_sequences([cleaned_text])

        print("Sequence:", sequence)

        # Padding
        padded = pad_sequences(
            sequence,
            maxlen=MAX_LEN,
            padding='post',
            truncating='post'
        )

        print("Padded Shape:", padded.shape)

        # Predict
        pred = model.predict(padded, verbose=0)

        print("Prediction Array:", pred)

        raw_score = float(pred[0][0])

        print("Raw Score:", raw_score)
        print("======================\n")

        # =========================
        # LABEL FIX
        # =========================
        # Many datasets use:
        # 0 = Spam
        # 1 = Ham (Not Spam)

        if raw_score >= THRESHOLD:
            prediction = "✅ Not Spam"
            confidence = f"{raw_score * 100:.2f}%"
        else:
            prediction = "🚫 Spam Message"
            confidence = f"{(1 - raw_score) * 100:.2f}%"

    return render_template(
        "index.html",
        prediction=prediction,
        confidence=confidence,
        raw_score=raw_score,
        user_input=user_input
    )

# =========================
# RUN APP
# =========================

if __name__ == "__main__":
    app.run(debug=True)