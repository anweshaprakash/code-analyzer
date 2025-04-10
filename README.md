# 🧠 Code Analyzer using Groq's Qwen 2.5 Coder

This is a lightweight CLI-based code analysis tool that utilizes Groq's `qwen-2.5-coder-32b` model via the OpenAI-compatible API. The purpose is to feed code into the LLM and get a structured analysis or error detection using LangChain for prompt composition.

---

## 🚀 Features

- Analyze local code files using LLMs
- Supports multiple languages: `.py`, `.js`, `.cpp`, `.java`, `.tex`
- Uses Groq’s blazing-fast inference API
- Leverages LangChain for prompt structuring

---

## 📁 Supported File Types

- Python (.py)
- JavaScript (.js)
- C++ (.cpp)
- Java (.java)
- LaTeX (.tex)

---

## 🔧 Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/your-username/code-analyzer-groq.git
cd code-analyzer-groq
```

### 2. Create and activate a virtual environment (optional but recommended)

```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Add your Groq API key

Create a `.env` file in the root directory and include:

```
groq_api_key=your_actual_groq_api_key_here
```

---

## ▶️ How to Run

Run the script:

```bash
python main.py
```

When prompted, paste the full path to your code file. Example:

```
PASTE YOUR CODE FILE PATH HERE: /home/user/Desktop/example.py
```

It will print the result of the analysis directly in the terminal.

---

## 🧠 How It Works

1. Loads Groq API key from `.env`
2. Accepts a file path via input
3. Reads file content and validates extension
4. Sends code to Groq API via OpenAI-compatible client
5. Wraps it in a system-human prompt using LangChain
6. Displays LLM-generated analysis

---

## 📦 File Structure

```
.
├── main.py             # Main code analyzer logic
├── .env                # Environment variables
├── requirements.txt    # Python dependencies
```

---

## 📋 Sample Prompt Flow

- **System Prompt**: Contextualizes the analysis
- **Human Prompt**: Asks specific questions like "State the errors in the code"

---

## 📄 License

MIT License. Free to use, modify, and distribute.

---

## ✨ Author

Made with ❤️ by Anwesha Prakash
