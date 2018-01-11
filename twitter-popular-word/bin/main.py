#!/usr/local/bin/python3

import os
import sys

sys.path.insert(0, os.path.abspath(
    os.path.dirname(os.path.realpath(__file__)) + '/../config'))
sys.path.insert(0, os.path.abspath(
    os.path.dirname(os.path.realpath(__file__)) + '/../lib'))

from config import Config
import logging.config

CONFIG = Config.get()
logging.config.dictConfig(CONFIG.LOG_CONFIG)
LOGGER = logging.getLogger("twitter-popular-word")
os.environ["TWITTER"] = CONFIG.CREDENTIALS_FILE

"""
#Needs to run once to download nltk data

import nltk
dl = nltk.downloader.Downloader("http://nltk.github.com/nltk_data/")
dl.download()

from nltk.twitter import Twitter

#Now we can start processing
tw = Twitter()
LOGGER.info("TW is {}".format(tw))
a = tw.tweets(keywords='love, hate',
              limit=10)
LOGGER.info("A is {}".format(a))


print ("\n\n\n")

tw = Twitter()
tw.tweets(follow=['759251', '612473'],
          stream=False,
          limit=10)
"""

from application import (get_tweets,
                         tweepy_get_tweets)

tweepy_get_tweets()
#get_tweets()
