import os
from google.genai import types

def write_file(working_directory, file_path, content):
    try:
        working_directory = os.path.abspath(working_directory)
        file_path = os.path.abspath(os.path.join(working_directory, file_path))

        if not file_path.startswith(working_directory):
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

        directory = os.path.dirname(file_path)
        if not os.path.exists(directory):
            os.makedirs(directory)

        with open(file_path, 'w') as f:
            f.write(content)

        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'

    except Exception as e:
        return f'Error: {e}'

schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Writes content to the specified file within the working directory. Overwrites the file if it already exists.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to the file to write to, relative to the working directory.",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The content to write to the file.",
            ),
        },
    ),
)
