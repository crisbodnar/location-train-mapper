#!/usr/bin/env python
from twitter import Twitter, OAuth
import csv
import sys
import urllib
import re
import requests
from itertools import izip
import codecs
import os
import json

#Setting up Twitter API
CONSUMER_KEY = 'tcNdxcZrQb6xvZRUOsg4PNH9R'
CONSUMER_SECRET = 'e2RvxTRAdu3ld6TKW3ymcrsdUVI8nOggU9dO1euSiwxxlGIKCW'
ACCESS_TOKEN = '1239954650-kI4Qf6BxxYRwz0thOKfz67YpDUqlORgWIk8PYUb'
ACCESS_SECRET = 'TIoci5kPZGikPWgaZtnCizPvBwGV8EwqoCPF3flZnRPmW'

oauth = OAuth(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET)

twitter = Twitter(auth = OAuth(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET))

#track=twitter&locations=-122.75,36.8,-121.75,37.8

example_co = [[-1.1498002, 51.2226126], [-1.039377, 51.2226126], [-1.039377, 51.3030391], [-1.1498002, 51.3030391]]

def cent(cood):
	lon = []
	lat = []
	for c in cood:
		lon.append(c[0])
		lat.append(c[1])
	f_ = sum(lon)/len(lon)
	s_ = sum(lat)/len(lat)
	return f_, s_

def extract_tweets(company):
	query_1 = twitter.search.tweets(q = '@' + company, count = 100, result_type = 'mixed')
	tweet_data = {}
	print("Search complete (%.3f seconds) %f" % (query_1["search_metadata"]["completed_in"], query_1["search_metadata"]['count']))
	for result in query_1["statuses"]:
		#print(result["text"])
		#print(result['created_at'])
		#print(result['id'])
		#print(result['place'])
		#print('\n')
		#tweet_data.append(result['id'])
		#tweet_data.append(result['created_at'])
		#tweet_data.append(result["text"])
		#tweet_data.append(result["place"])
		#print result['user']['id']
		#print result['user']['location']
		print(result["place"])
		if result["place"] is None:
			pass
		else:
			print(result['place'])
			tweet_data["id"] = result['id']
			tweet_data["created_at"] = result['created_at'].encode('utf-8')
			tweet_data["text"] = result['text'].encode('utf-8')
			tweet_data["coordinates"] = cent(result['place']['bounding_box']['coordinates'][0])
	return tweet_data
		
operators = []
#company_to_user("SouthernRailUK")
#extract_tweets("GWRHelp")

def write_to_file(tweet_data):
	with open('dict.csv', 'wb') as csv_file:
	    writer = csv.writer(csv_file)
	    for key, value in tweet_data.items():
	       writer.writerow([key, value])


write_to_file(extract_tweets("SouthernRailUK"))











