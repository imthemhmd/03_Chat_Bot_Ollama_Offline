import requests
import json


def call_ollama(prompt, stream=False):
    url = "http://localhost:11434/api/generate"
    model = 'qwen2.5-coder:7b'
    params = {
        'model':model,
        'prompt':prompt,
        'stream':stream
    }
    payload = json.dumps(params)
    response = requests.post(url, data=payload, headers={"Content-Type" : "application/json"})
    if response.status_code != 200:
        return "Error"
    else:
        return response.json()['response']

if __name__ == "__main__":
    prompt = input("Enter Your Question: ")
    model = 'qwen2.5-coder:7b'
    result = call_ollama(model, prompt)
    print(result)