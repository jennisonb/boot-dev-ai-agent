import os
import sys
import subprocess


def run_python_file(working_directory, file_path):
    abs_working_dir = os.path.abspath(working_directory)
    target_dir = abs_working_dir
    if file_path:
        target_dir = os.path.abspath(
            os.path.join(working_directory, file_path))
    if not target_dir.startswith(abs_working_dir):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(target_dir):
        return f'Error: File "{file_path}" not found.'
    if file_path[-3:] != ".py":
        return f'Error: "{file_path}" is not a Python file.'
    try:
        command = [sys.executable, target_dir]
        result = subprocess.run(
            command,
            text=True,
            cwd=abs_working_dir,
            stdout=subprocess.PIPE,  # Capture standard output
            stderr=subprocess.PIPE,  # Capture standard error
            timeout=30,
            # check=True  # Raise CalledProcessError for non-zero exit codes
        )
        if len(result.stdout) == 0 and len(result.stderr) == 0:
            return "No output produced."
        result_text = f"STDOUT: {result.stdout}\n"
        result_text += f"STDERR: {result.stderr}"
        if result.returncode != 0:
            result_text += f"\nProcess exited with code {result.returncode}"
        return result_text
    except Exception as e:
        return f"Error: running python: {e}"
