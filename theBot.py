# bot to post spaghetti pic scraped from web once every minute

import tweepy as tp
import time
import os

# login to twitter
api_key = ''
api_secret = ''
access_token = ''
access_secret = ''

# login to twitter api
auth = tp.OAuthHandler(api_key,api_secret)
auth.set_access_token(access_token,access_secret)
api = tp.API(auth)

#iterate over sketti pics
os.chdir('sketti_img')
for sketti_img in os.listdir('.'):
    api.update_with_media(sketti_img)
    time.sleep(60)
