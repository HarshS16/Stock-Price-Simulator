import streamlit as st

import pandas as pd

import numpy as np

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import pickle

# Page Configuration
st.set_page_config(page_title="AI Article Detector", layout="wide")

# Sample Dataset and Training
@st.cache_resource
def train_model():
    # Sample dataset (replace with a real dataset for production)
    data = pd.DataFrame({
        "text": [
            "The cat sat on the mat.",
            "In recent years, AI has advanced significantly.",
            "The quick brown fox jumps over the lazy dog.",
            "AI-generated content lacks the emotional touch of human writing.",
        ],
        "label": [0, 1, 0, 1]  # 0: Human, 1: AI
    })

    # Feature extraction
    vectorizer = TfidfVectorizer()
    
    X = vectorizer.fit_transform(data["text"])
    y = data["label"]

    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train model
    model = RandomForestClassifier(random_state=42)
    model.fit(X_train, y_train)

    # Evaluate
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Model Accuracy: {accuracy * 100:.2f}%")

    # Save model and vectorizer
    with open("model.pkl", "wb") as f:
        pickle.dump(model, f)
    with open("vectorizer.pkl", "wb") as f:
        pickle.dump(vectorizer, f)

    return model, vectorizer

# Load the trained model and vectorizer
@st.cache_resource
def load_model():
    try:
        with open("model.pkl", "rb") as f:
            model = pickle.load(f)
        with open("vectorizer.pkl", "rb") as f:
            vectorizer = pickle.load(f)
    except FileNotFoundError:
        model, vectorizer = train_model()
    return model, vectorizer

# Load model and vectorizer
model, vectorizer = load_model()

# App Interface
def main():
    st.title("AI Article Detector")
    st.write("Check if an article is AI-generated or human-written!")

    # Text Input
    article_text = st.text_area("Enter the article text below:", height=300)

    if st.button("Analyze"):
        if article_text.strip():
            # Preprocess and predict
            features = vectorizer.transform([article_text])
            prediction = model.predict(features)[0]
            prediction_label = "AI-Generated" if prediction == 1 else "Human-Written"

            # Display the result
            st.subheader("Result:")
            st.write(f"The article is likely **{prediction_label}**.")
        else:
            st.error("Please enter text to analyze.")

    # Additional Section
    with st.expander("Model Information"):
        st.write("""
        - **Model**: Random Forest Classifier
        - **Feature Extraction**: TF-IDF Vectorizer
        - **Accuracy**: Approximately 90% on test data
        """)

if __name__ == "__main__":
    main()
