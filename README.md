# AI Coding Agent

A portfolio project: an intelligent command-line coding assistant powered by Google's Gemini API.  
Inspired by agentic editors like Cursor and Claude Code, this tool demonstrates how LLMs can automate code understanding, navigation, and modification.

---

## 🚀 What is this project?

**AI Coding Agent** is a CLI tool that accepts natural language coding tasks and autonomously:
- Scans project files and directories
- Reads and writes file contents
- Executes Python scripts
- Iteratively plans and executes actions to solve coding problems

This project showcases practical AI integration, agentic workflows, and robust Python engineering.

---

## ✨ Features

- **Natural Language Interface:** Describe your coding task in plain English.
- **Automated Code Reasoning:** The agent plans and executes steps using Gemini's function calling.
- **File System Operations:** List, read, and write files securely.
- **Code Execution:** Run Python scripts and capture output.
- **Iterative Agent Loop:** The agent adapts its plan based on results, up to 20 steps per task.
- **Verbose Mode:** See each function call and agent decision for transparency.

---

## 🛠️ Technologies Used

- **Python 3.10+**
- **Google Gemini API**
- **dotenv** for environment management

---

## 🏁 Getting Started

1. **Clone the repository**
   ```
   git clone <your-repo-url>
   cd AI-AGENT
   ```

2. **Install dependencies**
   ```
   pip install -r requirements.txt
   ```

3. **Set up your Gemini API key**
   - Create a `.env` file in the project root:
     ```
     GEMINI_API_KEY=your_gemini_api_key_here
     ```

4. **Run the agent**
   ```
   python main.py "Describe your coding task here"
   ```
   Add `--verbose` for detailed agent output.

---

## 💡 Example Usage

```
python main.py "fix my calculator app, it's not starting correctly"
```
**Sample output:**
```
- Calling function: get_files_info
- Calling function: get_file_content
- Calling function: write_file
- Calling function: run_python_file
Final response:
Great! The calculator app now seems to be working correctly. The output shows the expression and the result in a formatted way.
```

---

## 📂 Project Highlights

- **Agentic Workflow:** Demonstrates how LLMs can chain function calls to solve real coding problems.
- **Safe File Handling:** All file operations are sandboxed to the working directory.
- **Extensible Design:** Easily add new agent functions or integrate with other APIs.
- **Educational Value:** Clear code and comments for learning or demonstration purposes.

---

## 📄 License

MIT License

---

*Built for learning, experimentation, and to showcase modern AI engineering.*
