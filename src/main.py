import os
import shutil
import streamlit as st

from ingest import ingest_documents 
from query import ask_question

DATA_FOLDER = "data"

os.makedirs(DATA_FOLDER, exist_ok=True)

st.set_page_config(
    page_title="Document Q&A Bot",
    page_icon="📚",
    layout="wide"
)

st.title("📚 AI Document Q&A Bot")

st.write("Upload PDF or DOCX files and ask questions about them.")

uploaded_files = st.file_uploader(
    "Upload Documents",
    type=["pdf", "docx"],
    accept_multiple_files=True
)

if uploaded_files:

    if st.button("Build Knowledge Base"):

        shutil.rmtree(DATA_FOLDER, ignore_errors=True)

        os.makedirs(DATA_FOLDER, exist_ok=True)

        for file in uploaded_files:

            with open(
                os.path.join(DATA_FOLDER, file.name),
                "wb"
            ) as f:

                f.write(file.read())

        with st.spinner("Building Vector Database..."):

            pages, chunks, total = ingest_documents()

        st.success("Knowledge Base Created")

        st.write(f"Pages : {pages}")

        st.write(f"Chunks : {chunks}")

        st.write(f"Database Size : {total}")

st.divider()

question = st.text_input("Ask a Question")

if st.button("Ask"):

    if question.strip() == "":

        st.warning("Enter a question.")

    else:

        with st.spinner("Searching Documents..."):

            result = ask_question(question)

        st.subheader("Answer")

        st.write(result["answer"])

        st.subheader("Sources")

        for source in result["citations"]:

            st.write("•", source)

        with st.expander("Retrieved Context"):

            st.text(result["context"])