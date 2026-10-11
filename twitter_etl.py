from httpx import Auth
import tweepy
import pandas as pd
from datetime import datetime, timedelta
import s3fs

#creating an api object
api = tweepy.API(Auth)


tweets = api.user_timeline(screen_name='elonmusk', count=100, tweet_mode='extended')


tweet_list = []
for tweet in tweets:
    text = tweet._json['full_text']

    refined_tweet = {
        'user': tweet.user.screen_name,
        'text': text,
        'retweet_count': tweet.retweet_count,
        'favorite_count': tweet.favorite_count,
        'created_at': tweet.created_at
    }
    tweet_list.append(refined_tweet)

df = pd.DataFrame(tweet_list)
df.to_csv('tweets.csv')
