import streamlit as st
import pickle
import re

# ============ تحميل النموذج و أداة TF-IDF ============
model = pickle.load(open("phishing_model.pkl", "rb"))
vectorizer = pickle.load(open("tfidf_vectorizer.pkl", "rb"))

# ============ دالة تنظيف النص ============
def clean_text(text):
    text = re.sub(r"http\S+|www\S+|https\S+", "", text)
    text = re.sub(r"[^a-zA-Z0-9\s]", "", text)
    text = text.lower()
    return text

# ============ واجهة المستخدم ============
st.title("📧 كاشف التصيّد في الإيميلات")
st.write("اكتب محتوى الإيميل ليتم تحليله ومعرفة ما إذا كان تصيّدًا إلكترونيًا.")

user_input = st.text_area("✉️ أدخل نص الإيميل هنا:")

if st.button("تحليل"):
    cleaned = clean_text(user_input)
    vect = vectorizer.transform([cleaned])
    prediction = model.predict(vect)[0]

    if prediction == 1:
        st.error("⚠️ هذا إيميل تصيّدي (Phishing)!")
    else:
        st.success("✅ هذا إيميل آمن (Legit).")
