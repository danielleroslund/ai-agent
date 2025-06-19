import os
import subprocess
from google.genai import types

def run_python_file(working_directory, file_path, args=None):
        working_directory = os.path.abspath(working_directory)
        file_path = os.path.abspath(os.path.join(working_directory, file_path))

        if not file_path.startswith(working_directory):
           return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

        if not os.path.isfile(file_path):
            filename = os.path.basename(file_path)
            return f'Error: File "{filename}" not found.'

        if not file_path.endswith('.py'):
            return f'Error: "{file_path}" is not a Python file.'
        try:
            commands = ["python", file_path]
            if args:
                commands.extend(args)
            result = subprocess.run(
                ['python3', file_path],
                cwd=working_directory,
                capture_output=True,
                text=True,
                timeout=30
            )

            output = []
            if result.stdout:
                output.append(f'STDOUT:\n{result.stdout}')
            if result.stderr:
                output.append(f'STDERR:\n{result.stderr}')

            if result.returncode != 0:
                output.append(f'Process exited with code {result.returncode}')
            
            return "\n".join(output) if output else "No output produced."
        except Exception as e:
            return f'Error: executing Python file: {e}'

schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Executes the specified Python file within the working directory and returns its output.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to the Python file to execute, relative to the working directory.",
            ),
        },
    ),
)
