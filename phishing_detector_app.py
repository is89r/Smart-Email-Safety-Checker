import streamlit as st
import pickle
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# ============ Load the model and vectorizer ============
model = pickle.load(open("phishing_model.pkl", "rb"))
vectorizer = pickle.load(open("tfidf_vectorizer.pkl", "rb"))

# ============ Text cleaning function ============
def clean_text(text):
    text = re.sub(r"http\S+|www\S+|https\S+", "", text)
    text = re.sub(r"[^a-zA-Z0-9\s]", "", text)
    text = text.lower()
    return text

# ============ Streamlit UI ============
st.set_page_config(page_title="Phishing Email Detector", page_icon="📧", layout="centered")

st.markdown("<h1 style='text-align: center; color: #4A90E2;'>🛡️ Smart Email Safety Checker</h1>", unsafe_allow_html=True)
st.write("Welcome! 🧑‍💻 Paste the content of any email below, and we'll help you detect if it's a phishing attempt or a safe message.")

with st.form("phishing_form"):
    user_input = st.text_area("📬 Email Content:", height=200, placeholder="Paste your email text here...")
    submitted = st.form_submit_button("🔍 Analyze Now")

    if submitted:
        if not user_input.strip():
            st.warning("🚨 Please enter some email content to analyze.")
        else:
            cleaned = clean_text(user_input)
            vect = vectorizer.transform([cleaned])
            prediction = model.predict(vect)[0]

            st.markdown("---")
            if prediction == 1:
                st.error("⚠️ This looks like a *Phishing Email*! Be cautious and avoid clicking any suspicious links.")
                st.markdown("💡 **Tip:** Always check the sender's email address and avoid sharing personal data.")
            else:
                st.success("✅ This email seems *Safe*. Nothing suspicious detected!")
                st.markdown("🎉 **Tip:** Stay alert anyway. Trust but verify!")

st.markdown("---")
st.caption("Made with ❤️ by Israa")
