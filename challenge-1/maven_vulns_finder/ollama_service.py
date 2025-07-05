import sys

import requests

import pom_utils

BASE_PROMPT = "Read the following pom file and summarize dependencies in json format (ignore example libraries)"

pom_content = pom_utils.read_file(sys.argv[1])

request_body = {
    "model": "llama3.2",
    "role": "java expert",
    "prompt": BASE_PROMPT + pom_content,
    "stream": False,
}

response = requests.post("http://localhost:11434/api/generate", json=request_body, proxies={"http": None, "https": None})
response_content = response.json()["response"]
dependency_list = pom_utils.get_dependency_list(response_content)

