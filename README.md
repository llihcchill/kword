# kword
Webscraper that scrapes all text from a website and organises it into its keywords for an API fuzzing list.

# Installation
All you need to do is install the python script using the git command below:  
`git clone https://github.com/llihcchill/kword`  

## Setting up related words functionality (-r flag)
  
If you plan to use the related words function (-r), you will need to have credits on your ChatGPT account and will need to make an API key [here](https://platform.openai.com/api-keys).  
Then you will need to edit the kword.py script and replace (in the ai_api_request() function) "your api key" with your generated one:  

![image](https://github.com/llihcchill/kword/assets/125551072/12ffaba5-a4b9-4913-b7f3-6d10958f9efc)  

or altenatively (and more safely), you can use the library [python-dotenv](https://pypi.org/project/python-dotenv/) to save your API key in an environment variable. The variable should be OPENAI_API_KEY="your api key" and by leaving the OpenAi() object parameters blank, it should work.

  
# Usage
There are three arguments for this script (not including help), of which the main one is to of course scrape a URL and return a list of keywords:  
`python kword.py -u https://<url>`  

---

The list can be appended to an output file using the -o flag:  
`python kword.py -u https://<url> -o output.txt`  

---

At a moments notice, you can use the -r flag to request an AI chatbot to provide a list of related words. You can request as many words as need be by adding them together with commas:  
(*note that putting the words together with commas is very important*)  
`python kword.py -r test,lab,experiment`
