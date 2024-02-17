import tweepy
import requests
import json
import random
from PIL import Image

def listtostring(s):
 
    # initialize an empty string
    str1 = "\n"
 
    # return string
    return (str1.join(s))

# authenticate twitter account

client = tweepy.Client(
    consumer_key="0nOpHhG2N2w9J9ldXK70fJpb2",
    consumer_secret="qXBvpPMR6wpS9Y3rqJK4D8ThvQV4pGE4iQYajz7ZNPmM5QWtLP",
    access_token="1688859028158566400-ua5L2IUnD1E66ev2S9WFesL2k2TT98",
    access_token_secret="QqH2Wc7rTf7UPiEE6Tfv7lrFzs5tvFbhQ03oZlqJm9t3e"
)

auth = tweepy.OAuth1UserHandler(
   "0nOpHhG2N2w9J9ldXK70fJpb2", "qXBvpPMR6wpS9Y3rqJK4D8ThvQV4pGE4iQYajz7ZNPmM5QWtLP",
   "1688859028158566400-ua5L2IUnD1E66ev2S9WFesL2k2TT98", "QqH2Wc7rTf7UPiEE6Tfv7lrFzs5tvFbhQ03oZlqJm9t3e"
)
api = tweepy.API(auth)

#tweet number facts and cat facts

querystring = {"fragment":"true","notfound":"floor","json":"true"}

headers = {
	"X-RapidAPI-Key": "2ae9382820mshbeb98204cef46bdp1b5769jsn85bde535876e",
	"X-RapidAPI-Host": "numbersapi.p.rapidapi.com"
}

i=0
while i <= 0:
    
    num = random.randint(0,200000)
    url = f"https://numbersapi.p.rapidapi.com/{num}/trivia"
    response = requests.get(url, headers=headers, params=querystring)
    api_response = json.loads(response.text)

    with open('A.txt','r+') as file1:
        
        file1r = file1.read()
        A = file1r.split("\n")
        
        if api_response['number'] not in A:
            
            A.append(api_response['number'])
            A = listtostring(A)
            file1.truncate(0)
            file1.seek(0)
            file1.write(A)
            
            txt1 = f"number : {num}\n{api_response['text']}\n\n#number_facts"
            
            client.create_tweet(text=txt1)
        
        else:
            i = i