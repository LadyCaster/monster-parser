import re
import os
import requests
from bs4 import BeautifulSoup
import unicodedata

def main():
    text = get_text(open_url(input(str())))
    with open('monster_texts.txt', 'a') as file:
         file.write(text + '\n')

def open_url(url):
    headers = {
        'user-agent':
            'Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:38.0)'
            ' Gecko/20100101 Firefox/38.0',
    }
    s = requests.Session()
    response = s.get(url, headers=headers, timeout=20)
    html = str(response.text)
    return html

def get_text(html):
    description = re.search(
        r'JobDescription[\s\S]*?>([\s\S]*?)<footer', html)
    description = description.group(1) if description else ""
    description = BeautifulSoup(description, "lxml").text
    clean_text = unicodedata.normalize("NFKD",description)
    return clean_text

if __name__ == "__main__":
    main()
