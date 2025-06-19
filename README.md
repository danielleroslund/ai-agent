# AI Coding Agent

A command-line AI agent that can analyze, modify, and run code using Google's Gemini API. Inspired by agentic editors like Cursor and Claude Code.

## Features

- Accepts natural language coding tasks
- Scans directories and files
- Reads and writes file contents
- Executes Python files
- Uses Gemini API for reasoning and planning

## Getting Started

1. **Install dependencies:**
   ```
   pip install -r requirements.txt
   ```

2. **Set your Gemini API key:**
   - Create a `.env` file in the project root:
     ```
     GEMINI_API_KEY=your_gemini_api_key_here
     ```

3. **Run the agent:**
   ```
   python main.py "your coding task here"
   ```

   Add `--verbose` for more detailed output.

## Example

```
python main.py "fix my calculator app, it's not starting correctly"
```

## License

MIT License

---

*Built for educational purposes*
