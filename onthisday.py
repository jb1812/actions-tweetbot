import tweepy
import requests
import datetime
import os

# authenticate twitter account

client = tweepy.Client(
    consumer_key=os.getenv("API_KEY"),
    consumer_secret=os.getenv("API_KEY_SECRET"),
    access_token=os.getenv("ACCESS_TOKEN"),
    access_token_secret=os.getenv("ACCESS_TOKEN_SECRET")
)

#tweet on this day facts

date = datetime.datetime.now()
api_url = 'https://api.api-ninjas.com/v1/historicalevents?month={}&day={}'.format(date.strftime("%m"), date.strftime("%d"))
response = requests.get(api_url, headers={'X-Api-Key': "mEWcITGkxLzXHpcJo0bjPARdYumKoVDhdrpteRN3"})
url_response = response.text
a =  list(eval(url_response))
i = 0
while i <= len(a)-1:
    txt3 = 'Day: {} {}\n\nOn this day in the year {}, {}\n\n#OnThisDay #History'.format(date.strftime("%d"), date.strftime("%B"), a[i]['year'], a[i]['event'])
    client.create_tweet(text=txt3)
    i = i + 1
