import tweepy
import requests
import os

def listtostring(s):
    str1 = "\n"
    return (str1.join(s))

# authenticate twitter account

client = tweepy.Client(
    consumer_key=os.getenv("API_KEY"),
    consumer_secret=os.getenv("API_KEY_SECRET"),
    access_token=os.getenv("ACCESS_TOKEN"),
    access_token_secret=os.getenv("ACCESS_TOKEN_SECRET")
)

auth = tweepy.OAuth1UserHandler(
   os.getenv("API_KEY"), os.getenv("API_KEY_SECRET"),
   os.getenv("ACCESS_TOKEN"), os.getenv("ACCESS_TOKEN_SECRET")
)
api = tweepy.API(auth)

#tweet cat facts

i=0
while i == 0:
    
    fact = requests.get("https://catfact.ninja/fact?max_length=280").json()
    img = requests.get("https://api.sefinek.net/api/v2/random/animal/cat").json()
    data = requests.get(img['message']).content
    f = open('cats.jpg','wb') 
    f.write(data)
    f.close()
           
    with open('cats.txt','r+') as file2:
        
        file2r = file2.read()
        cats = file2r.split("\n")
        
        if fact['fact'] not in cats:
            
            cats.append(fact['fact'])
            cats = listtostring(cats)
            file2.truncate(0)
            file2.seek(0)
            file2.write(cats)
            
            txt2 = f"{fact['fact']}\n\n#Cat_Facts #CatsOfTwitter"
            
            cats = api.media_upload(filename='cats.jpg')
            media_id = media.media_id
            
            client.create_tweet(text=txt2, media_ids=[media_id])
            i = 1
            
        else:
            i = i
