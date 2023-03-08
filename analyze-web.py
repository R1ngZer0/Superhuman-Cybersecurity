import openai
import os
import requests
from bs4 import BeautifulSoup

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
        max_tokens=500,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    text = response['choices'][0]['text'].strip()
    return text
    
def scrape_content(url):
    page_content = requests.get(url)
    soup = BeautifulSoup(page_content.text, 'html.parser')
    content = soup.get_text()
    return content
    
url = 'https://threatgen.com'

webinfo = repr(scrape_content(url))
save_file("webcontent.txt", webinfo)
print(webinfo)

prompt = open_file("prompt4.txt").replace('<<FEED>>', webinfo)
output = gpt_3(prompt)
print(output)
save_file("web-analysis.txt", output)
        


