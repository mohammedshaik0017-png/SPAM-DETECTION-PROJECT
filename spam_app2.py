import streamlit as st
import pandas as pd
import re
import string
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score
)

st.set_page_config(
    page_title="SMS Spam Detection",
    page_icon="📩",
    layout="centered"
)

st.markdown("""
<style>

.main{
    background-color:#f5f7ff;
}

.title{
    text-align:center;
    font-size:42px;
    font-weight:bold;
    color:#2c3e50;
}

.sub{
    text-align:center;
    color:#555;
    font-size:18px;
}

</style>
""", unsafe_allow_html=True)

st.markdown(
    "<div class='title'>📩 SMS Spam Detection App</div>",
    unsafe_allow_html=True
)

st.markdown(
    "<div class='sub'>Machine Learning Based Spam Classifier</div>",
    unsafe_allow_html=True
)

# ======================
# LOAD LOCAL DATASET
# ======================

df = pd.read_csv("spam.csv", encoding="latin-1")

df = df[["v1", "v2"]]

df.rename(
    columns={
        "v1": "label",
        "v2": "message"
    },
    inplace=True
)

df["label"] = df["label"].map({
    "ham": 0,
    "spam": 1
})
def clean_text(text):

    text = text.lower()

    text = re.sub(
        f"[{string.punctuation}]",
        "",
        text
    )

    return text

df["clean_message"] = df["message"].apply(clean_text)

vectorizer = TfidfVectorizer(
    stop_words="english"
)

X = vectorizer.fit_transform(
    df["clean_message"]
)

y = df["label"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = LogisticRegression(
    max_iter=1000
)

model.fit(
    X_train,
    y_train
)

pred = model.predict(X_test)

accuracy = accuracy_score(y_test, pred)
precision = precision_score(y_test, pred)
recall = recall_score(y_test, pred)
f1 = f1_score(y_test, pred)

st.markdown("## 📊 Model Performance")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Accuracy", round(accuracy, 2))
col2.metric("Precision", round(precision, 2))
col3.metric("Recall", round(recall, 2))
col4.metric("F1 Score", round(f1, 2))

if "prediction_history" not in st.session_state:
    st.session_state.prediction_history = []

st.markdown("## ✉️ Check Your Message")

user_input = st.text_area(
    "Enter SMS Message"
)

col1, col2 = st.columns(2)

predict_btn = col1.button("🚀 Predict")
clear_btn = col2.button("🧹 Clear")

if clear_btn:
    st.rerun()
if predict_btn:

    if user_input.strip() == "":

        st.warning("Please enter a message.")

    else:

        cleaned = clean_text(user_input)

        vector = vectorizer.transform(
            [cleaned]
        )

        result = model.predict(vector)[0]

        probability = model.predict_proba(vector)[0]

        spam_prob = round(
            probability[1] * 100,
            2
        )

        ham_prob = round(
            probability[0] * 100,
            2
        )

        if result == 1:

            st.error(
                "🚨 SPAM MESSAGE DETECTED"
            )

            prediction_result = "Spam"

        else:

            st.success(
                "✅ SAFE MESSAGE"
            )

            prediction_result = "Ham"

        st.write(
            f"Spam Probability: {spam_prob}%"
        )

        st.write(
            f"Ham Probability: {ham_prob}%"
        )

        st.session_state.prediction_history.append({
            "Message": user_input,
            "Result": prediction_result
        })

        st.markdown(
            "## 📈 Message Probability Chart"
        )

        fig, ax = plt.subplots()

        ax.pie(
            [spam_prob, ham_prob],
            labels=["Spam", "Ham"],
            autopct="%1.1f%%"
        )

        st.pyplot(fig)

if len(st.session_state.prediction_history) > 0:

    st.markdown(
        "## 📝 Prediction History"
    )

    history_df = pd.DataFrame(
        st.session_state.prediction_history
    )

    st.dataframe(history_df)

st.markdown("## 📂 Upload CSV File")

uploaded_file = st.file_uploader(
    "Choose CSV File",
    type=["csv"]
)

if uploaded_file is not None:

    uploaded_data = pd.read_csv(
        uploaded_file
    )

    st.dataframe(
        uploaded_data.head()
    )