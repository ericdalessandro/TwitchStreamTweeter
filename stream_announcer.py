import tweepy, twitch, time

# Tweepy and Twitch-python libraries both needed to access the appropriate APIs.

# Twitter access keys for Twitter API
ACCESS_TOKEN = ''
ACCESS_TOKEN_SECRET = ''
CONSUMER_KEY =  ''
CONSUMER_SECRET = ''

# Twitch access keys for Twitch API
TWITCH_CLIENT = ''

# Setup API access
helix = twitch.Helix(TWITCH_CLIENT)
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)
user = helix.user('') # Twitch user name

hasTweeted = False
stream_link = 'https://twitch.tv/hedgi'

def check_live_status():
    global hasTweeted
    print('Checking stream status...')
    # Checks if the Twitch stream is live
    if user.is_live and not hasTweeted:
        print('User is live. Initiating grace period...')
        time.sleep(900) # 900 seconds is a 15 minute grace period before it checks for Tweet
        print('Checking Twitter Feed...')
        latest_tweet = api.user_timeline(tweet_mode='extended')
        latest_tweet = latest_tweet[0].full_text
        print(latest_tweet)

        # Search for link in latest tweet.
        if 'https://' in latest_tweet:
            print('Tweet already made.')
            hasTweeted = True
        # Send tweet if no link is found.
        else:
            print('No Announcement found. Making announcement...')
            print('Tweet: ' +
                  user.display_name + ' is live at ' + stream_link + ' streaming ' + user.stream.title + '!')
            api.update_status(
                user.display_name + ' is live at ' + stream_link + ' streaming ' + user.stream.title + '!'
            )
            hasTweeted = True

    # Resets the hasTweeted variable when stream ends to allow for future use.
    elif not user.is_live and hasTweeted:
        hasTweeted = False

    elif not user.is_live and not hasTweeted:
        print("No stream found.")


while True:
    check_live_status()
    time.sleep(60)
