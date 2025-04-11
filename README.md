# 📧 Smart Email Phishing Detector

Welcome to the **Email Phishing Detector** — a user-friendly app that helps detect whether an email is **safe** or **phishing** with just one click! 🚨

Built using `Python`, `Streamlit`, and `scikit-learn`.

---

## 🌟 Features

- Detect phishing emails based on their content.
- Friendly and simple web interface.
- Real-time feedback and safety tips.

---

## 🧠 How it Works

1. We trained a Logistic Regression model on real email data.
2. The email content is cleaned and vectorized using `TF-IDF`.
3. The model predicts whether the input is phishing (1) or safe (0).

---

## 🖥️ Try the App

👉 [Click here to try the live app](https://your-username.streamlit.app)

> Replace the link above with your actual Streamlit Cloud URL.

---

## 🛠️ How to Run Locally

```bash
# Clone the repo
git clone https://github.com/your-username/phishing-email-detector
cd phishing-email-detector

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run phishing_detector_app.py
