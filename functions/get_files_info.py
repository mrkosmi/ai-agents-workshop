import os
def get_files_info(working_dir: str, directory_path: str) -> str:
    abs_working_dir = os.path.abspath(working_dir)

    path = os.path.abspath(
        os.path.join(abs_working_dir, directory_path)
    )

    if not path.startswith(abs_working_dir):
        return f'Error: Cannot access "{directory_path}" outside working directory'
    
    if not os.path.exists(path):
        return f"Directory '{path}' does not exist."
    
    if not os.path.isdir(path):
        return f"'{path}' is not a directory."
    
    files = os.scandir(path)

    files_info = []
    for file in files:
        content = file.name
        size = file.stat().st_size
        is_dir = file.is_dir()
        files_info.append(f"- {content}: file_size={size} bytes, is_dir={is_dir}\n")
    return "".join(files_info)
