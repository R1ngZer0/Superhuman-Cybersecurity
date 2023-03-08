import openai
import os

def open_file(filepath):
    with open(filepath, 'r', encoding='UTF-8') as infile:
        return infile.read()
        
def save_file(filepath, content):
    with open(filepath, 'w', encoding='UTF-8') as outfile:
        outfile.write(content)
        

openai.api_key = open_file("openai-key.txt")

prompt = open_file("prompt.txt")

response = openai.Completion.create(
    model="text-davinci-003",
    prompt=prompt,
    temperature=1.0,
    max_tokens=500,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
)

text = response
print(text)