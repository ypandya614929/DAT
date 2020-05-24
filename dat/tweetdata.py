import tweepy
import operator
import re
from collections import Counter
from collections import OrderedDict
from operator import itemgetter

# Consumer keys and access tokens, used for OAuth
consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Creation of the actual interface, using authentication
api = tweepy.API(auth)

class Tweetdata(object):

	def userdata(self, uid):

		l=list()

		udata = api.user_timeline(screen_name = uid, count = 400)

		for tweet in udata:
			l.append(tweet.text)

		return l

	def hashdata(self, temp):

		l=list()

		for tweet in tweepy.Cursor(api.search, q=temp).items(10):
			l.append(tweet.text)

		return l

	def timedata(self, uid):

		udata = api.user_timeline(screen_name = uid, count = 10)

		d=dict()

		for i in range(1,25):
			if i<10:
				i='0'+str(i)
			if str(i) not in d:
				d[str(i)]=0

		for tweet in udata:
			t=str(tweet.created_at).split(" ")
			t1=str(t[1]).split(":")
			if t1[0] not in d:
				d[t1[0]]=1
			else:
				d[t1[0]]+=1

		sorted_d = sorted(d.items(), key=operator.itemgetter(0))

		return sorted_d

	def urldata(self, uid):

		l=list()

		udata = api.user_timeline(screen_name = uid, count = 100)

		for tweet in udata:
			t=tweet.text.encode('utf-8')
			urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', str(t))
			for url in urls:
				l.append(url.strip('\']'))

		return l

	def sourcedata(self, temp):

		l=list()

		for tweet in tweepy.Cursor(api.search, q=temp).items(10):
			l.append(tweet.source)

		counts = Counter(l)
		final=list()
		name=dict()

		for key, value in counts.items():
			final.append(value)
			name.update({key:value})

		final.sort(reverse=True)

		d = OrderedDict(sorted(name.items(), key=itemgetter(1),reverse=True))
		OrderedDict(d)

		return d
