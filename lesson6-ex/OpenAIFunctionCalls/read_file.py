def read_file(file_path):
    """Read file content."""
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except FileNotFoundError:
        return f"[Error] File not found: {file_path}"
    except Exception as e:
        return f"[Error] Errors during reading file: {e}"
