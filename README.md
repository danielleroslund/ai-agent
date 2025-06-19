# AI Coding Agent

A toy version of an agentic AI code assistant, inspired by tools like Cursor and Claude Code, built using Google's free Gemini API.

## What Does the Agent Do?

This CLI tool:
- Accepts a coding task (e.g., "fix my calculator app, it's not starting correctly")
- Chooses from a set of predefined functions to work on the task, such as:
  - Scanning files in a directory
  - Reading a file's contents
  - Overwriting a file's contents
  - Executing the Python interpreter on a file
- Repeats these steps until the task is complete (or fails)

**Example usage:**
```
python main.py "fix my calculator app, its not starting correctly"
# Calling function: get_files_info
# Calling function: get_file_content
# Calling function: write_file
# Calling function: run_python_file
# Calling function: write_file
# Calling function: run_python_file
# Final response:
# Great! The calculator app now seems to be working correctly. The output shows the expression and the result in a formatted way.
```

## Prerequisites

- Python 3.10+ installed
- Access to a Unix-like shell (e.g., zsh or bash)
- A Gemini API key

## Learning Goals

- Introduce you to multi-directory Python projects
- Show how AI tools work under the hood
- Practice Python and functional programming skills

## Setup

1. **Clone the repository:**
   ```
   git clone <your-repo-url>
   cd <your-repo-directory>
   ```

2. **Install dependencies:**
   ```
   pip install -r requirements.txt
   ```

3. **Set up your Gemini API key:**
   - Create a `.env` file in the project root:
     ```
     GEMINI_API_KEY=your_api_key_here
     ```

4. **Run the agent:**
   ```
   python main.py "your coding task here"
   ```

   Add `--verbose` for more detailed output.

## Project Structure

- `main.py` — Main entry point and agent loop
- `prompts.py` — System prompt for the agent
- `call_function.py` — Function call implementations

## License

MIT License

---

*Built for educational purposes*
