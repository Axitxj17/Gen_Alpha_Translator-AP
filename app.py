import streamlit as st
import pandas as pd
from src.utils import load_slang
from src.translator import alpha_to_beta

st.set_page_config(page_title="Gen Alpha Translator", layout="wide")
slang_dict = load_slang("data/slang_dict.json")

st.title("Gen Alpha Translator")
st.write("Understand Gen Alpha in seconds!")
input_text = st.text_area("Enter Gen Alpha text here:", height=200)

if st.button("Translate"):
    if input_text.strip() == "":
        st.warning("Please enter some text to translate.")
    else:
        translated_text, usage_counts = alpha_to_beta(input_text, slang_dict)
        
        st.subheader("Translated Text")
        st.text_area("Beta Translation:", value=translated_text, height=200)
        
        st.subheader("Slang Usage Counts")
        usage_df = pd.DataFrame(list(usage_counts.items()), columns=["Slang", "Count"])
        st.dataframe(usage_df)


