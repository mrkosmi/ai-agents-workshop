import os
def write_file(working_directory: str, file_path: str, content: str) -> str:
    try:
        abs_working_dir = os.path.abspath(working_directory)

        path = os.path.abspath(
            os.path.join(abs_working_dir, file_path)
        )

        if not path.startswith(abs_working_dir):
            return f'Error: Cannot access "{file_path}" outside working directory'
        
        if os.path.isdir(path):
            return f"Error: '{path}' is a directory, not a file."

        parent_dir = os.path.dirname(path)
        os.makedirs(parent_dir, exist_ok=True)

        with open(path, 'w', encoding='utf-8') as file:
            file.write(content)
        
        return f"File has been written successfully."
    
    except PermissionError:
        return f"Error: Permission denied when trying to write to '{file_path}'."
    except Exception as e:
        return f"Error writing file: {str(e)}"