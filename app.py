import streamlit as st
import re
from collections import Counter
from nltk.corpus import stopwords
import nltk

# Download stopwords (only first time)
nltk.download("stopwords")

def top_10_words_from_text(text):
    text = text.lower()
    words = text.split(" ")

    cleaned_words = []

    for word in words:
        match = re.match(r'^[a-z]+', word)
        if match is not None:
            cleaned_words.append(match.group())

    stop_words = set(stopwords.words("english"))

    without_stop_words = []
    for word in cleaned_words:
        if word not in stop_words:
            without_stop_words.append(word)

    word_count = Counter(without_stop_words)
    return word_count.most_common(10)


# ---------------- Streamlit UI ---------------- #

st.title("📊 Top 10 Words Finder")
st.write("Upload a text file and get the top 10 most frequent words (without stopwords).")

uploaded_file = st.file_uploader("Upload a .txt file", type=["txt"])

if uploaded_file is not None:
    text = uploaded_file.read().decode("utf-8")
    
    top10 = top_10_words_from_text(text)

    st.subheader("Top 10 Words")
    
    for word, count in top10:
        st.write(f"**{word}** : {count}")