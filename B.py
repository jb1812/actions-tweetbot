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
    
    fact = requests.get("https://catfact.ninja/fact?max_length=280").json()
    img = requests.get("https://api.sefinek.net/api/v2/random/animal/cat").json()
    data = requests.get(img['message']).content
    f = open('media.jpg','wb') 
    f.write(data)
    f.close()
           
    with open('B.txt','r+') as file2:
        
        file2r = file2.read()
        B = file2r.split("\n")
        
        if fact['fact'] not in B:
            
            B.append(fact['fact'])
            B = listtostring(B)
            file2.truncate(0)
            file2.seek(0)
            file2.write(B)
            
            txt2 = f"{fact['fact']}\n\n#cat_facts"
            
            media = api.media_upload(filename='media.jpg')
            media_id = media.media_id
            
            client.create_tweet(text=txt2, media_ids=[media_id])
            i = i + 1
            
        else:
            i = i