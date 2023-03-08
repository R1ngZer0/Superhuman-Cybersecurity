import openai
import os

def open_file(filepath):
    with open(filepath, 'r', encoding='UTF-8') as infile:
        return infile.read()
        
def save_file(filepath, content):
    with open(filepath, 'w', encoding='UTF-8') as outfile:
        outfile.write(content)
        
openai.api_key = open_file('openai-key.txt')
        
def gpt_3 (prompt):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=600,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    text = response['choices'][0]['text'].strip()
    return text

file = input("Enter a file name: ")
feed = open_file(file)
prompt = open_file("prompt3.txt").replace('<<INPUT>>', feed)
analysis = gpt_3(prompt)
print(analysis)
save_file("analysis-output.txt", analysis)
