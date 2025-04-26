import sys

import requests

url = "https://api.openai.com/v1/chat/completions"

headers = {"Authorization": "",
           "Content-Type": "application/json"}

if len(sys.argv) == 3:
    data = {
        "model": "gpt-4o-mini",
        "messages": [
            {"role": "system", "content": sys.argv[1]},
            {"role": "user", "content": sys.argv[2]}
        ], "temperature": 0.7
    }

    response = requests.post(url, headers=headers, json=data)
    print(response.json()["choices"][0]["message"]["content"])