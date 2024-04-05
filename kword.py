import sys
import requests
from bs4 import BeautifulSoup
from openai import OpenAI

h = False
h_index = 0
url = False
u_index = 0
output = False
o_index = 0
related = False

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

def ai_api_request():
    words = sys.argv[2]
    words = words.replace(",", ", ")

    client = OpenAI(api_key="your api key")

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a linguist writing an API endpoint list that contains only one word on each line of the list, it is all in lower case, but you need some words to then elaborate on and find related words to those words."},
            {"role": "user", "content": f"Can you write a list that contains words related to the following words: {words}"}
        ]
        
    )

    return completion.choices[0].message

def create_output_file(write_to_file):
    with open(str(sys.argv[o_index + 1]), "w") as file:
        file.write(write_to_file)
        print("List successfully created!")


help = "KWORD HELP \n \n ======== \n \n -u: URL to be webscraped \n -r: Keyword to be expanded upon via the ChatGPT API \n -o: Makes an output to a file \n \n Example usage: python kword.py -u <host url> -o list.txt"

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

def run():
    if h == True:
        print(help)
        return

    if related == True:
        if len(sys.argv) > 5:
            print("For the AI API request, please combine all words together: -r test,lab,experiment")
            return

        if output != True:
            print(ai_api_request())
            return

        create_output_file(ai_api_request())
        return
    
    if output != True and related != True:
        print(webscrape_filter())
        return

    create_output_file(webscrape_filter())

run()
