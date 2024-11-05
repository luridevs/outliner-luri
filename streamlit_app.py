import streamlit as st
import openai
from transformers import AutoTokenizer, AutoModel
from sentence_transformers import SentenceTransformer, util
import pinecone  # For vector storage and RAG pipeline
import faiss

st.title("Outliner")
st.write(
    "Tired of looking through and re-reading your notes for hours? Just put in the new notes you've taken, or start from scratch anytime, and Outliner will come up with a comprehensive, thorough outline."
)


