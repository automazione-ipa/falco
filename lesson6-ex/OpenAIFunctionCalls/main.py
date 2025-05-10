import sys

from open_ai import call_openai_api

url = "https://api.openai.com/v1/chat/completions"

functions = [
    {
        "name": "read_file",
        "description": "Read file content in a given path.",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "File path to read"
                }
            },
            "required": ["file_path"]
        }
    },
    {
        "name": "wiki_search",
        "description": "Research by words on wikipedia.",
        "parameters": {
            "type": "object",
            "properties": {
                "wiki_search_words": {
                    "type": "string",
                    "description": "Words to search on Wikipedia"
                }
            },
            "required": ["wiki_search_words"]
        }
    },
    {
        "name": "calculate",
        "description": "Math expression evaluation.",
        "parameters": {
            "type": "object",
            "properties": {
                "expression": {
                    "type": "string",
                    "description": "Expression to evaluate"
                }
            },
            "required": ["expression"]
        }
    }
]

# set OPENAI_TOKEN in system env
# usage: python main.py "esperto di animali" "descrivi in modo semplice l'ornitorinco prendendo informazioni da wikipedia"
if len(sys.argv) == 3:
    response = call_openai_api(url, sys.argv[1], sys.argv[2], functions)
    print(response["choices"][0]["message"]["content"])

