from twitterData import *


class runTwitterData:
	def __init__(self, twitterUser):

		# Which user?
		self.userData = twitterData(twitterUser)

		# Profile Information
		self.name = userData.getName()
		self.description = userData.getDescription()
		self.location = userData.getLocation()
		self.twitterUsername = userData.getTwitterUsername()
		self.websiteURL = userData.getWebsiteURL()
		self.profileImageURL = userData.getProfileImageURL()
		self.profileBannerURL = userData.getProfileBannerURL()
		self.profileCreatedAt = userData.getCreatedAt()
		self.geoEnabled = userData.getGeoEnabled()

		# Types of Tweets
		self.allTweets = userData.getFormattedTweets()
		self.mediaTweets = userData.getMediaTweets()
		self.badTweets = userData.getBadTweets()