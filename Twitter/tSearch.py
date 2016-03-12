from TwitterSearch import *
import csv

try:
    tuo = TwitterUserOrder('jaydub475') # create a TwitterUserOrder

    # it's about time to create TwitterSearch object again
    ts = TwitterSearch(
        consumer_key = 'yVvPHQPI4VkWFyoaxQpkgTd0e',
        consumer_secret = 'ZbBVdqC1Hw0Wy7Fabbi4YicTczIF9R6sKLhN7ml2ep4yi4xwhC',
        access_token = '51730914-Wf9lj3LaeFPY4XxPm2U8l73LWybcOxBq3rl2N5H5f',
        access_token_secret = '7UoeJZJu5nfYKRw8hD4UZh7VMpjeGkeb0OWbt5oZNIojU',
    )

    imageList = []
    blockedWords = []
    badTweets = []

    with open('blockwords.csv', 'r') as csvfile:
        wordReader = csv.reader(csvfile)

        for word in wordReader:  
            blockedWords.append(word)

    blockedWords = blockedWords[0]
    ex = False

    limit = 10

    # start asking Twitter about the timeline
    for tweet in ts.search_tweets_iterable(tuo):
        #print( '@%s tweeted: %s' % ( tweet['user']['screen_name'], tweet['text'] ))

        tweetText = tweet['text']
        for x in blockedWords:
            break
            if str(x) in tweetText:
                ex = True
                badTweets.append('@%s tweeted: %s' % ( tweet['user']['screen_name'], tweet['text'] ))

        try:
            imageList.append(tweet['entities']['media'][0]['media_url'])
        except KeyError:
            pass

        try: 
            name = tweet['user']['name']
        except KeyError:
            name = 'Unobtainable'

        try:
            description = tweet['user']['description']
        except KeyError:
            description = 'Unobtainable'

        try:
            location = tweet['user']['location']
        except KeyError:
            location = 'Unobtainable'

        try:
            screen_name = tweet['user']['screen_name']
        except KeyError:
            screen_name = 'Unobtainable'

        try:
            website = tweet['user']['entities']['url']['urls'][0]['expanded_url']
        except KeyError:
            website = 'Unobtainable'

        try:
            profile_image_url = tweet['user']['profile_image_url']
        except KeyError:
            profile_image_url = 'Unobtainable'

        try:
            created_at = tweet['user']['created_at']
        except KeyError:
            created_at = 'Unobtainable'

        try:
            geo_enabled = tweet['user']['geo_enabled']
        except KeyError:
            geo_enabled = False

        try:
            profile_banner_url = tweet['user']['profile_banner_url']
        except KeyError:
            profile_banner_url = 'Unobtainable'

        limit -= 1
        if limit == 0:
            break


    print('Name: ' + name)
    print('Description: ' + description)
    print('Location: ' + location)
    print('Screen Name: ' + screen_name)
    print('Website: ' + website)
    print('Profile Image URL: ' + profile_image_url)
    print('Profile Banner URL: ' + profile_banner_url)
    print('Profile Created: ' + created_at)
    print('Geo-location Enabled? ' + str(geo_enabled))
    print('Image URLs: ')

    print(imageList)

    for t in badTweets:
        print(badTweets)

    print(blockedWords)
    print(ex)


except TwitterSearchException as e:
    print(e)
