import json
import os

import requests

from read_file import read_file
from wiki_search import wiki_search


def call_openai_api(api_url, role, question, functions=None):
    """Invoke OpenAI."""
    headers = {
        "Authorization": os.getenv('OPENAI_TOKEN'),
        "Content-Type": "application/json"
    }
    data = {
        "model": "gpt-4o-mini",
        "messages": [
            {"role": "system", "content": role},
            {"role": "user", "content": question}
        ], "temperature": 0.7
    }
    if functions:
        data['functions'] = functions
    data['function_call'] = 'auto'
    response = requests.post(api_url, headers=headers, json=data, proxies={"http": None, "https": None})
    response.raise_for_status()

    response_message = response.json()["choices"][0]["message"]
    if response_message.get("function_call"):
        """
            if OpenAI thinks that a function call should be invoked: 
            the function call name and arguments were passed through the response
        """
        function_name = response_message["function_call"]["name"]
        function_args = json.loads(response_message["function_call"]["arguments"])

        if function_name == "read_file":
            file_content = read_file(file_path=function_args["file_path"])
            data['messages'].append(
                {
                    "role": "function",
                    "name": function_name,
                    "content": json.dumps(file_content),
                }
            )

            data = {
                "model": "gpt-4o-mini",
                "messages": data['messages'],
                "temperature": 0.7,
            }

        if function_name == "wiki_search":
            print("[Words]: " + str(function_args))
            wiki_sum = wiki_search(wiki_search_words=function_args["wiki_search_words"])
            data['messages'].append(
                {
                    "role": "function",
                    "name": function_name,
                    "content": json.dumps(wiki_sum),
                }
            )

            data = {
                "model": "gpt-4o-mini",
                "messages": data['messages'],
                "temperature": 0.7,
            }

        if function_name == "calculate":
            print("[expression]: " + str(function_args))
            result = eval(function_args["expression"])
            data['messages'].append(
                {
                    "role": "function",
                    "name": function_name,
                    "content": json.dumps(result),
                }
            )

            data = {
                "model": "gpt-4o-mini",
                "messages": data['messages'],
                "temperature": 0.7,
            }

        response = requests.post(api_url, headers=headers, json=data, proxies={"http": None, "https": None})
        response.raise_for_status()
        response_data = response.json()

        return response_data
