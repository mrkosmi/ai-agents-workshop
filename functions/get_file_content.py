import os
def get_file_content(working_dir: str, file_path: str) -> str:
    abs_working_dir = os.path.abspath(working_dir)

    path = os.path.abspath(
        os.path.join(abs_working_dir, file_path)
    )

    if not path.startswith(abs_working_dir):
        return f'Error: Cannot access "{file_path}" outside working directory'
    
    if not os.path.exists(path):
        return f"File '{path}' does not exist."
    
    if not os.path.isfile(path):
        return f"'{path}' is not a file."
    
    with open(path, 'r') as file:
        content = file.read()
    
    return content or "File is empty."