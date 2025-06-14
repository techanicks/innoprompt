import streamlit as st
import cohere

# Set your Cohere API key directly here
co = cohere.Client("VsZZLL1D2ygAj8KoDrpgVZRVdkpTzXhLVIDgc9Mc")

# Page configuration
st.set_page_config(page_title="InnoPrompt - AI Innovation Helper", page_icon="💡", layout="wide")

# App title and header
st.markdown(
    """
    <h1 style='text-align: center; color: #2E86C1;'>💡 InnoPrompt</h1>
    <h4 style='text-align: center; color: #1C2833;'>AI-powered innovative idea generator</h4>
    <hr style='border:1px solid #AED6F1'>
    """,
    unsafe_allow_html=True
)

# Problem input area
st.markdown("### 🤔 Enter a real-world problem:")
user_input = st.text_area("Describe a challenge you'd like to solve", height=150)

# Generate ideas button
if st.button("🚀 Generate Innovative Ideas"):
    if not user_input.strip():
        st.warning("Please enter a problem description.")
    else:
        with st.spinner("Thinking creatively..."):
            try:
                response = co.generate(
                    model='command-r-plus',
                    prompt=f"Suggest three innovative solutions to the following problem:\n{user_input}",
                    max_tokens=300,
                    temperature=0.8
                )
                ideas = response.generations[0].text.strip()
                st.success("✅ Here are some AI-generated innovative ideas:")
                st.text_area("📋 Innovative Ideas", ideas, height=200)
            except Exception as e:
                st.error(f"Something went wrong: {e}")

# Footer with your name
st.markdown(
    """
    <hr style='border:1px solid #D5DBDB'>
    <p style='text-align: center; color: #808B96;'>Created by Orga Hemen George 💻</p>
    """,
    unsafe_allow_html=True
)
