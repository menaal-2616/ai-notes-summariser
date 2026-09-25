import streamlit as st

st.set_page_config(page_title="AI Notes Summariser")
st.title("AI-Powered Notes Summariser 📝")
st.caption("Built by Menaal | Python + NLP")

st.divider()

notes_input = st.text_area("Paste your notes here:", height=200, placeholder="Paste your long notes, lecture transcript or article here...")

if st.button("Generate Summary"):
    if notes_input.strip() == "":
        st.warning("Please paste some notes first.")
    else:
        sentences = [s.strip() for s in notes_input.split('.') if len(s.strip()) > 20]
        sentences.sort(key=len, reverse=True)
        
        # Take top 2 most informative sentences
        summary = '. '.join(sentences[:2]) + "."

        st.subheader("Summary")
        st.success(summary)

        col1, col2 = st.columns(2)
        col1.metric("Original Sentences", len(sentences))
        col2.metric("Summary Sentences", 2)

st.divider()
st.write("Tech Stack: Python, Streamlit, NLP (Extractive Summarization)")