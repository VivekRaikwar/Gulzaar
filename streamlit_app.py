import os
import streamlit as st
from groq import Groq

def generate_gulzar_style_poetry(insult_target):
    client = Groq(api_key="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")  # Add your API key here
    
    prompt = f"Compose a poetic insult in the style of Gulzar, filled with depth and lyrical beauty, directed at {insult_target}. Use rich metaphors and Urdu/Hindi elegance."
    
    chat_completion = client.chat.completions.create(
        messages=[
            {"role": "user", "content": prompt}
        ],
        model="llama-3.3-70b-versatile",
    )
    
    return chat_completion.choices[0].message.content

st.title("Gulzar-style Poetic Insult Generator")
insult_target = st.text_input("Kise zaleel karna hai? (Enter target for insult):")

if st.button("Generate Insult"):
    if insult_target:
        poetry_insult = generate_gulzar_style_poetry(insult_target)
        st.subheader("Gulzar-style poetic insult:")
        st.write(poetry_insult)
    else:
        st.warning("Please enter a target for the insult.")
