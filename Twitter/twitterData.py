from TwitterSearch import *
import csv


class twitterData:
	def __init__(self, twitterUser):

		try:
			self.tuo = TwitterUserOrder(twitterUser)

			self.ts = TwitterSearch(
			    # KEYS HERE
			)

		except TwitterSearchException as e:
		    print(e)

		# Variables
		self.allTweets = []
		self.mediaTweets = []
		self.formattedTweets = []
		self.blockedWords = []
		self.badTweets = []
		self.twitterUser = twitterUser

		# Run functions
		self.addToBlockedWords()
		self.storeInfo()


	def storeInfo(self):

		for tweet in self.ts.search_tweets_iterable(self.tuo):
			try:
				self.personalName = tweet['user']['name']
			except KeyError:
				self.personalName = None

			try: 
				self.description = tweet['user']['description']
			except KeyError:
				self.description = None

			try:
				self.twitterHandle = tweet['user']['screen_name']
			except KeyError:
				self.twitterHandle = None

			try:
				self.message = tweet['text']
			except KeyError:
				self.message = None

			try:
				self.people = tweet['contibutors']
			except KeyError:
				self.people = None

			try:
				self.location = tweet['place']
			except KeyError:
				self.location = None

			try: 
				self.websiteURL = tweet['user']['entities']['url']['urls'][0]['expanded_url']
			except KeyError:
				self.websiteURL = None

			try: 
				self.profileImageURL = tweet['user']['profile_image_url']
			except KeyError:
				self.profileImageURL = None

			try: 
				self.profileBannerURL = tweet['user']['profile_banner_url']
			except KeyError:
				self.profileBannerURL = None

			try: 
				self.geoEnabled = tweet['user']['geo_enabled']
			except KeyError:
				self.geoEnabled = None

			try: 
				self.createdAt = tweet['user']['created_at']
			except KeyError:
				self.createdAt = None

			if self.geoEnabled == True:
				# find locations
				pass

			if self.tweetedMedia(tweet) == False:
				self.tweetType = 'No media included'
			else:
				self.tweetType = 'Media included'

			try:
				self.tweetLink = None
			except:
				self.tweetLink = None

			try:
				self.date = None
			except KeyError:
				self.date = None

			toCheck = tweet['user']

			self.formatTweets(self.personalName, self.twitterHandle, self.message, self.people, self.location, self.date, self.tweetType, self.tweetLink)
			self.tweetedMedia(tweet)

		print(toCheck)

	def formatTweets(self, pName, tHandle, msg, ppl, loc, date, tType, tLink):
		source = 'Twitter'

		tweetData = {
		'source': source,
		'type': tType,
		'name': pName,
		'username': tHandle,
		'text': msg,
		'date': date,
		'location': loc,
		'people': ppl,
		'tweet link': tLink
		}

		self.formattedTweets.append(tweetData)

	def getFormattedTweets(self):
		return self.formattedTweets

	def getName(self):
		return self.personalName

	def getDescription(self):
		return self.description

	def getLocation(self):
		return self.location

	def getTwitterUsername(self):
		return self.twitterHandle

	def getWebsiteURL(self):
		return self.websiteURL

	def getProfileImageURL(self):
		return self.profileImageURL

	def getProfileBannerURL(self):
		return self.profileBannerURL

	def getCreatedAt(self):
		return self.createdAt

	def getGeoEnabled(self):
		return self.geoEnabled

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

	def getBadTweets(self):
		tweetNum = 0

		for eachTweet in self.formattedTweets:
			tweetText = self.formattedTweets[tweetNum]['text']
			if self.pickBadTweets(eachTweet, tweetText) == True:
				self.badTweets.append(tweetText)
			tweetNum += 1

		return self.badTweets

	def tweetedMedia(self, tweet):
		try: 
			self.mediaTweets.append(tweet['entities']['media'][0]['media_url'])
		except KeyError:
			return False

	def getMediaTweets(self):
		return self.mediaTweets










