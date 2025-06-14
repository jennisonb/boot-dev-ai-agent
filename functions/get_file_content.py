import os
MAX_CHARS = 10000


def get_file_content(working_file_path, file_path):
    abs_working_dir = os.path.abspath(working_file_path)
    target_dir = abs_working_dir
    if file_path:
        target_dir = os.path.abspath(
            os.path.join(working_file_path, file_path))
    if not target_dir.startswith(abs_working_dir):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(target_dir):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    try:
        with open(target_dir, "r") as f:
            file_content_string = f.read()
            if len(file_content_string) > MAX_CHARS:
                trunc_file_content = file_content_string[:MAX_CHARS] + f'[...File "{file_path}" truncated at 10000 characters]'
                return trunc_file_content
            else:
                return file_content_string
    except Exception as  e:
        return f"Error: reading file: {e}"
    
