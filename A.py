import tweepy
import requests
import json
import random
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

#tweet number facts

querystring = {"fragment":"true","notfound":"floor","json":"true"}

headers = {
	"X-RapidAPI-Key": "RAPID_API_KEY",
	"X-RapidAPI-Host": "numbersapi.p.rapidapi.com"
}

i=0
while i == 0:
    
    num = random.randint(0,50000000)
    url = f"https://numbersapi.p.rapidapi.com/{num}/trivia"
    response = requests.get(url, headers=headers, params=querystring)
    api_response = json.loads(response.text)

    with open('A.txt','r+') as file1:
        
        file1r = file1.read()
        A = file1r.split("\n")
        
        if api_response.get('text','none') not in A:
            
            A.append(api_response.get('text','none'))		
            A = listtostring(A)
            file1.truncate(0)
            file1.seek(0)
            file1.write(A)
            num = format(int(api_response['number']), ',d')
            
            txt1 = f"number : {num}\n\n{api_response.get('text','none')}.\n\n#number_facts"
            
            client.create_tweet(text=txt1)
            
            i = 1

        else:
            i = i
