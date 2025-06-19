# AI Code Assistant

This is an AI-powered coding agent that can answer questions about your codebase, run code, and perform file operations using the Gemini API.

## Features

- List files and directories
- Read file contents
- Execute Python files with optional arguments
- Write or overwrite files
- Step-by-step reasoning and explanations

## Usage

1. **Install dependencies:**
   ```
   pip install -r requirements.txt
   ```

2. **Set your Gemini API key:**
   - Create a `.env` file in the project root:
     ```
     GEMINI_API_KEY=your_api_key_here
     ```

3. **Run the assistant:**
   ```
   python main.py "your question here"
   ```
   Example:
   ```
   python main.py "How does the calculator render results to the console?"
   ```

4. **Verbose mode:**
   ```
   python main.py "your question here" --verbose
   ```

## Project Structure

- `main.py` — Main entry point and agent loop
- `prompts.py` — System prompt for the agent
- `call_function.py` — Function call implementations

## License

MIT License

---

*Created for educational purposes.*
