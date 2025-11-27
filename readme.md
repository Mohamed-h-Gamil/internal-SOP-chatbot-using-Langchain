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

- **Context-Aware Answers**: Strictly grounded in *maids_cc_sop_comprehensive.txt*.
- **Source Citations**: UI highlights the exact document section retrieved.
- **Dual Interface**: CLI for testing + Chainlit Web UI for end users.
- **Fast Retrieval**: Uses FAISS for lightweight, local vector search.

---

## 🛠️ Tech Stack

- **Framework**: LangChain  
- **LLM & Embeddings**: Google Gemini 2.5 Flash  
- **Vector Store**: Chromadb
- **Interface**: Chainlit  
- **Language**: Python 3.10+

---

## ⚙️ Setup & Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/internal-sop-chatbot.git
cd internal-sop-chatbot
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

*Make sure you have:*  
`langchain`, `langchain-google-genai`, `chromadb`, `chainlit`

### 3. Configure Credentials

You need a Google Gemini API Key:

```bash
export GOOGLE_API_KEY="your_api_key_here"
```

---

## 🏃‍♂️ How to Run

### **Option 1: Web Interface (Recommended)**

Launch the web application:

```bash
chainlit run chat_ui.py -w
```

### **Option 2: CLI Tool**

Run the terminal version:

```bash
python sop_chatbot.py
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
