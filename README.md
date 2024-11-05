# Outliner Tool for Law Students

## Overview
The Outliner tool is designed for law students to compile and organize their course notes into a structured outline. Outlines are essential study tools for law students, summarizing key concepts, cases, and rules covered in each class. This tool intelligently processes and organizes notes, making it accessible and helpful for students with disabilities who may need extra time and support.

## Features
- **Automatic Note Organization**: Upload notes and let the tool automatically structure them into a coherent outline.
- **Fine-Tuning and Personalization**: Fine-tunes on existing outlines based on course name, term, and university, making the outline accurate and relevant.
- **RAG (Retrieval-Augmented Generation) Pipeline**: When new notes are added, the tool appends them to the existing outline in the correct section or reorganizes them as necessary.
- **Search and Retrieval**: Query specific topics or cases to get relevant outline sections.

## Requirements
- Python 3.7+
- Streamlit
- OpenAI API (for LLM, optional)
- Pinecone (for vector storage and retrieval)
- Sentence Transformers library
- Transformers library (for tokenizer and model loading)

## Setup

1. Clone this repository.
   ```bash
   git clone https://github.com/yourusername/outliner-tool.git
