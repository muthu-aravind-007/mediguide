# 🏥 MediGuide – AI Healthcare Research Assistant

## Overview

MediGuide is an AI-powered healthcare research assistant that uses Retrieval-Augmented Generation (RAG), multilingual support, image understanding, and knowledge graph visualization to help users explore complex healthcare and research topics.

## Key Features

### 1. Healthcare Research Assistant
- Uses RAG to retrieve relevant information from medical and research datasets.
- Answers domain-specific questions using retrieved context.
- Supports conversational follow-up questions.

### 2. Multilingual Support
- Automatically detects the user's language.
- Supports multiple languages, including Tamil and Hindi.
- Translates queries and responses to enable multilingual interaction.

### 3. Image Understanding
- Accepts image uploads.
- Uses Google Gemini API to analyze and describe uploaded images.
- Supports image-based queries.

### 4. Dynamic Concept Visualization
- Extracts key concepts using an LLM.
- Builds interactive knowledge graphs dynamically.
- Visualizes relationships between concepts, such as "uses", "contains", and "depends on".

### 5. Research Explorer
- Searches and retrieves relevant research content.
- Includes arXiv research papers alongside healthcare information.

## Tech Stack

- **Frontend:** Streamlit
- **Language:** Python
- **LLMs:** Mistral via Ollama, Google Gemini API
- **RAG:** Sentence Transformers, NumPy, Scikit-learn
- **Knowledge Graph:** NetworkX, PyVis
- **Other:** Google Gemini API, multilingual translation, VADER Sentiment Analysis

## Run Locally

```bash
git clone https://github.com/muthu-aravind-007/ai-multi-domain-chatbot.git
cd ai-multi-domain-chatbot
pip install -r requirements.txt
streamlit run app.py
```

## Example Queries

- Explain how diabetes develops.
- What is machine learning?
- Explain the role of insulin in the human body.
- Upload an image and ask for an explanation.

## Project Outcome

MediGuide combines healthcare information retrieval, multilingual interaction, image understanding, and interactive concept visualization in one AI-powered application.

## 👤 Author

**A. Muthu Aravind**
