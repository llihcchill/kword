# kword
Webscraper that scrapes all text from a website and organises it into its keywords for an API fuzzing list.

# Installation
All you need to do is install the python script using the git command below:  
`git clone https://github.com/llihcchill/kword`

# Usage
There are three arguments for this script (not including help), of which the main one is to of course scrape a URL and return a list of keywords:  
`python kword.py -u https://<url>`

---

The list can be appended to an output file using the -o flag:  
`python kword.py -u https://<url> -o output.txt`

---

At a moments notice, you can use the -r flag to request an AI chatbot to provide a list of related words. You can request as many words as need be as more arguments:  
*at the time of writing this function has not been finished yet*  
`python kword.py -r test lab experiment`
