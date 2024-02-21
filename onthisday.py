import tweepy
import requests
import datetime
import time

# authenticate twitter account

client = tweepy.Client(
    consumer_key="0nOpHhG2N2w9J9ldXK70fJpb2",
    consumer_secret="qXBvpPMR6wpS9Y3rqJK4D8ThvQV4pGE4iQYajz7ZNPmM5QWtLP",
    access_token="1688859028158566400-ua5L2IUnD1E66ev2S9WFesL2k2TT98",
    access_token_secret="QqH2Wc7rTf7UPiEE6Tfv7lrFzs5tvFbhQ03oZlqJm9t3e"
)

#tweet on this day facts

date = datetime.datetime.now()

api_url = 'https://api.api-ninjas.com/v1/historicalevents?month={}&day={}'.format(date.strftime("%m"), date.strftime("%d"))
response = requests.get(api_url, headers={'X-Api-Key': '9l9YTdwVRO2oB8V02nL7lQ==Fsdgu0G40N7RBwiG'})
url_response = response.text
a =  list(eval(url_response))

i = 0
while i <= len(a)-1:
    
    txt3 = 'Day: {} {}\n\nOn this day in the year {}, {}\n\n#OnThisDay #History'.format(date.strftime("%d"), date.strftime("%B"), a[i]['year'], a[i]['event'])
    print(txt3)
    client.create_tweet(text=txt3)
    time.sleep(900)
    i = i + 1