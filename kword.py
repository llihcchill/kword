import sys
import requests
from bs4 import BeautifulSoup

h = False
h_index = 0
url = False
u_index = 0
output = False
o_index = 0

def webscrape(url):
    website_content = requests.get(url).text
    soup = BeautifulSoup(website_content, "html.parser")
    
    for data in soup(["style", "script"]):
        data.decompose()

    return '\n'.join(soup.stripped_strings)

def webscrape_filter():
    data = webscrape(sys.argv[u_index + 1])
    data = str(data.lower())
    filter = open("filter.txt", "r")

    for line in range(1, 49):
        filter_word = str(filter.readline())

        if data.find(filter_word[:]) > 0:
            data = data.replace(filter_word, "\n")

    return data


help = "KWORD HELP \n \n ======== \n \n -u: URL to be webscraped \n -ai: Keyword to be expanded upon via an AI API \n -o: Makes an output to a file \n \n Example usage: python kword.py -u <host url> -o list.txt"

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

    if sys.argv[i] == "-r":
        related = True
        r_index = i

def run():
    if h == True:
        print(help)
        return

    if output != True:
        print(webscrape_filter())
        return

    with open(str(sys.argv[o_index + 1]), "w") as file:
        file.write(webscrape_filter())
        print("List successfully created!")

run()
