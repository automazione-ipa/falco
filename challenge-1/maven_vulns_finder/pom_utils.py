import json
import re


def read_file(file_path):
    """
    :param file_path: file path
    :return: file content
    """
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except FileNotFoundError:
        return f"[Error] File not found: {file_path}"
    except Exception as e:
        return f"[Error] Errors during reading file: {e}"


def get_dependency_list(model_response):
    """
    :param model_response: pom dependencies in json format
    :return: dictionary list (dependency list)
    """
    if "```json" not in model_response:
        model_response = model_response.replace("```", "```json", 1)
    return json.loads(re.search("```json(.*)```", model_response, re.DOTALL).group(1))
