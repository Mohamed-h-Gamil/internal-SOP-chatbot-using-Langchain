# Internal SOP Chatbot using Langchain

A RAG-based AI assistant designed to automate internal employee queries regarding Standard Operating Procedures (SOPs), Visa Rules, and Compliance Fees.

---

## 📖 Project Overview

This project solves the operational bottleneck of employees constantly asking HR/Managers for factual compliance information. Instead of searching through dense PDF manuals, staff can ask the bot natural language questions.

The system utilizes Retrieval-Augmented Generation (RAG) to:

- Ingest a raw text SOP document (simulated internal policies)
- Retrieve the exact section relevant to the user's query
- Generate a precise, cited answer using Google Gemini

---

## 🚀 Key Features

- **Context-Aware Answers**: Strictly grounded in *data/SOP.pdf*.
- **Dual Interface**: CLI for testing + Chainlit Web UI for end users.
- **Fast Retrieval**: Uses Chromadb for lightweight, local vector search.

---

## 🛠️ Tech Stack

- **Framework**: LangChain  
- **LLM & Embeddings**: Google Gemini 2.5 Flash lite
- **Vector Store**: Chromadb
- **Interface**: Chainlit  
- **Language**: Python 3.10+

---

## ⚙️ Setup & Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Mohamed-h-Gamil/internal-SOP-chatbot-using-Langchain
cd internal-SOP-chatbot-using-Langchain
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure Credentials

You need a Huggingface and Google Gemini API Key stored in a .env file or:

```bash
export GOOGLE_API_KEY="your_api_key_here"
```

### 4. Prepare the Vector Database

```bash
python data_preprocessing.py
```

---

## 🏃‍♂️ How to Run

### **Option 1: Web Interface (Recommended)**

Launch the web application:

```bash
chainlit run sop_chat_chainlit.py -w
```

### **Option 2: CLI Tool**

Run the terminal version:

```bash
python sop_chat_cli.py
```

---

## 🧪 Example Scenarios to Test

- **“What is the minimum salary for a Filipino maid?”**  
  → Should cite the 1,500 AED rule.

- **“Does a maid from Kenya need police clearance?”**  
  → Confirms requirement + validity period.

- **“What are the fees for a failed medical test?”**  
  → Explains refund or replacement policy.

---
