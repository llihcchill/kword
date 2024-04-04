import sys
import io
import requests
from bs4 import BeautifulSoup

def webscrape(url):
    website_content = requests.get(url).content
    soup = BeautifulSoup(website_content, "html.parser")
    
    for data in soup(["style", "script"]):
        data.decompose()

    return '\n'.join(soup.stripped_strings)


help = "KWORD HELP \n \n ======== \n \n -u: URL to be webscraped \n -ai: Keyword to be expanded upon via an AI API \n -o: Makes an output to a file \n \n Example usage: python kword.py -u <host url> -o list.txt"

h = False
h_index = 0
url = False
u_index = 0
output = False
o_index = 0

for i in range(1, len(sys.argv)):
    if sys.argv[i] == "--help" or sys.argv[i] == "-h":
        h = True
        h_index = i
        

    if sys.argv[i] == "-o":
        output = True
        o_index = i
    
    if sys.argv[i] == "-u":
        url = True
        u_index = i

def run():
    if h == True:
        print(help)
        return

    if output != True:
        print(webscrape(sys.argv[u_index]))
        return

    with open(str(sys.argv[o_index + 1]), "w") as file:
        file.write(webscrape(sys.argv[u_index]))

run()
