#!/usr/bin/env python
import random
import json
import os
from twython import Twython

twitter = None

def find_env_variable(env_var_to_find):
    """Finds an environment variable returns true if found, returns false if not"""
    try:
        env_var = os.environ[env_var_to_find]
        return env_var
    except KeyError:
        return False


def send_tweet(tweet_text):
    """Uses the Twython client instance to send a tweet"""
    twitter.update_status(status = tweet_text)


def handler(event,context):
    """Sends random tweet from list of potential tweets"""
    tweet = setup_and_get_tweet()
    send_tweet(tweet)


def setup_and_get_tweet():
    """Setup of the variables used for credentials and Twython instance.
    Also returns the tweet passed into environment from the lambda environment
    variables, unless one wasn't provided in which case it takes a random tweet
    and returns that."""

    DEBUG = find_env_variable('debug')
    TWEET = find_env_variable('tweet')

    # Loads in 'creds.json' values as a dictionary
    with open('creds.json') as creds:
        credentials = json.loads(creds.read())

    # Sets config values from the config file
    CONSUMER_KEY = credentials["consumer_key"]
    CONSUMER_SECRET = credentials["consumer_secret"]
    ACCESS_TOKEN_KEY = credentials["access_token_key"]
    ACCESS_TOKEN_SECRET = credentials["access_token_secret"]
    if DEBUG:
        print('consumer key: {} \n'
              'consumer secret: {} \n'
              'access token key: {} \n'
              'access token secret: {}'.format(CONSUMER_KEY, CONSUMER_SECRET,
                                               ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET))

    # Create the Twython Twitter client using our credentials
    # Global is used so that if any other methods need the Twython instance it will be available
    global twitter
    twitter = Twython(CONSUMER_KEY, CONSUMER_SECRET,
                      ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET)
    # Random tweets list
    potential_tweets = [
        'Very fresh tweet',
        'Golly, no tweet provided! Gonna Pick a random one now ^_^',
        'I sure am tweeting it up right now',
        'I am the senate',
        'This sure is a massive collection of tweets'
    ]
    # Checks if TWEET has been set return that else once of our random tweets
    return TWEET if TWEET else random.choice(potential_tweets)


# test when running python file as script
if __name__ == '__main__':
    handler('event','context')