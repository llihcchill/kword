import sys
import requests
from bs4 import BeautifulSoup

def webscrape(url):
    website_content = requests.get(url).content
    soup = BeautifulSoup(website_content, "html.parser")
    
    for data in soup(["style", "script"]):
        data.decompose()

    return '\n'.join(soup.stripped_strings)

help = "KWORD HELP \n \n ======== \n \n -u: URL to be webscraped \n -ai: Keyword to be expanded upon via an AI API \n -o: Makes an output to a file \n \n Example usage: python kword.py -u <host url> -o list.txt"

if sys.argv[1] == "--help":
    print(help)

if sys.argv[1] == "-h":
    print(help)

if sys.argv[1] == "-u":
    print(webscrape(sys.argv[2]))
