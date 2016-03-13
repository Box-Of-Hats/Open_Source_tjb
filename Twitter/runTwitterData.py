from twitterData import *

userData = twitterData('Rhiannonnnn_')

tweets = userData.Tweets()

for tweet in tweets:
	print(tweet)
	print()