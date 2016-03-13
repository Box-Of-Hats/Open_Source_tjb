from TwitterSearch import *
import csv


class twitterData:
	def __init__(self, twitterUser):
		self.allTweets = []
		self.mediaTweets = []
		self.formattedTweets = []
		self.blockedWords = []
		self.badTweets = []
		self.twitterUser = twitterUser
		self.addToBlockedWords()

		try:
			self.tuo = TwitterUserOrder(self.twitterUser)

			self.ts = TwitterSearch(
				consumer_key = 'yM5VzvXl7YhDOTpiGR6VGy3Kf',
				consumer_secret = 'mtRmoTKY28XSUU5qdYAWw73YnhFc85zhzOkFpPXDFcccPtL2hs',
				access_token = '159593120-FzaltKk0wvFUSfR4BQyF2pqr7obQ2Jtr0lDO0uPj',
				access_token_secret = '0EXUwZOZsJX4wvqjsc6iNTExngxrujZnF6QeCSONkX4xs',
			)

		except TwitterSearchException as e:
		    print(e)

	def Tweets(self):

		for tweet in self.ts.search_tweets_iterable(self.tuo):
			try:
				personalName = tweet['user']['name']
			except KeyError:
				personalName = None

			try:
				twitterHandle = tweet['user']['screen_name']
			except KeyError:
				twitterHandle = None

			try:
				message = tweet['text']
			except KeyError:
				message = None

			try:
				people = tweet['contibutors']
			except KeyError:
				people = None

			try:
				location = tweet['place']
			except KeyError:
				location = None

			try:
				date = None
			except KeyError:
				date = None

			self.formatTweets(personalName, twitterHandle, message, people, location, date)

		tweetNum = 0

		for eachTweet in self.formattedTweets:
			tweetText = self.formattedTweets[tweetNum]['text']
			if self.pickBadTweets(eachTweet, tweetText) == True:
				print(tweetText)
			tweetNum += 1


	def formatTweets(self, pName, tHandle, msg, ppl, loc, date,):
		source = 'Twitter'

		tweetData = {
		'source': source,
		'type': None,
		'name': pName,
		'username': tHandle,
		'text': msg,
		'date': date,
		'location': loc,
		'people': ppl
		}

		self.formattedTweets.append(tweetData)

	def addToBlockedWords(self):
		with open('blockwords.csv', 'r') as csvfile:
			wordReader = csv.reader(csvfile)
			for word in wordReader:  
				self.blockedWords.append(word)

		self.blockedWords = self.blockedWords[0]

	def pickBadTweets(self, Tweet, tweetText):
		for x in self.blockedWords:
			if str(x) in tweetText:
				return True

	def name(self):
		finito = False

		while finito == False:
			for tweet in self.ts.search_tweets_iterable(self.tuo):
				try: 
					name = tweet['user']['name']
				except KeyError:
					name = 'Unobtainable'
				finito = True


	def description(self):
		finito = False

		while finito == False:
			for tweet in self.ts.search_tweets_iterable(self.tuo):
				try: 
					name = tweet['user']['description']
				except KeyError:
					name = 'Unobtainable'
				finito = True

	def location(self):
		finito = False

		while finito == False:
			for tweet in self.ts.search_tweets_iterable(self.tuo):
				try: 
					name = tweet['user']['location']
				except KeyError:
					name = 'Unobtainable'
				finito = True

	def twitterUsername(self):
		finito = False

		while finito == False:
			for tweet in self.ts.search_tweets_iterable(self.tuo):
				try: 
					name = tweet['user']['screen_name']
				except KeyError:
					name = 'Unobtainable'
				finito = True

	def websiteURL(self):
		finito = False

		while finito == False:
			for tweet in self.ts.search_tweets_iterable(self.tuo):
				try: 
					name = tweet['user']['entities']['url']['urls'][0]['expanded_url']
				except KeyError:
					name = 'Unobtainable'
				finito = True

	def profileImageURL(self):
		finito = False

		while finito == False:
			for tweet in self.ts.search_tweets_iterable(self.tuo):
				try: 
					name = tweet['user']['profile_image_url']
				except KeyError:
					name = 'Unobtainable'
				finito = True

	def profileBannerURL(self):
		finito = False

		while finito == False:
			for tweet in self.ts.search_tweets_iterable(self.tuo):
				try: 
					name = tweet['user']['profile_banner_url']
				except KeyError:
					name = 'Unobtainable'
				finito = True

	def createdAt(self):
		finito = False

		while finito == False:
			for tweet in self.ts.search_tweets_iterable(self.tuo):
				try: 
					name = tweet['user']['created_at']
				except KeyError:
					name = 'Unobtainable'
				finito = True

	def geoEnabled(self):
		finito = False

		while finito == False:
			for tweet in self.ts.search_tweets_iterable(self.tuo):
				try: 
					name = tweet['user']['geo_enabled']
				except KeyError:
					name = 'Unobtainable'
				finito = True

	def tweetLink(self):
		pass

	def tweetedMedia(self, tweet):
		try: 
			self.mediaTweets.append(tweet['entities']['media'][0]['media_url'])
		except KeyError:
			pass

	def getMediaTweets(self):
		mediaTweets = self.mediaTweets

		return mediaTweets










