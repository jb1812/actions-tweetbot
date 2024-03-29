import tweepy
import requests
import json
import random
import os

# authenticate twitter account

client = tweepy.Client(
    consumer_key=os.getenv("API_KEY"),
    consumer_secret=os.getenv("API_KEY_SECRET"),
    access_token=os.getenv("ACCESS_TOKEN"),
    access_token_secret=os.getenv("ACCESS_TOKEN_SECRET")
)

def listtostring(s):
    str1 = "\n"
    return (str1.join(s))

#tweet number facts

querystring = {"fragment":"true","notfound":"floor","json":"true"}

headers = {
	"X-RapidAPI-Key": os.getenv("RAPID_API_KEY"),
	"X-RapidAPI-Host": "numbersapi.p.rapidapi.com"
}

i=0
while i == 0:
    
    num = random.randint(0,100000000)

    with open('number.txt','r+') as file1:
        
        file1r = file1.read()
        number = file1r.split("\n")
        
        if num not in number:

            num = str(num)
            number.append(num)
            number = listtostring(number)
            file1.truncate(0)
            file1.seek(0)
            file1.write(number)

            url = f"https://numbersapi.p.rapidapi.com/{num}/trivia"
            response = requests.get(url, headers=headers, params=querystring)
            api_response = json.loads(response.text)
            response_list = list(api_response.values())
            
            num = format(int(response_list[1]), ',d')
            cap = response_list[0][0].upper() + response_list[0][1:]
            txt1 = f"Number : {num}\n\n{cap}.\n\n#Number_Facts #Maths #Fun_Fact"

            client.create_tweet(text=txt1)
            
            i = 1
        else:
            i = 0
