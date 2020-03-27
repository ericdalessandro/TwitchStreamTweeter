# TwitchStreamTweeter
Checks to see if a Twitch Stream is live and after a grace period, will automatically announce the stream on Twitter if no announcement has been found.

This bot utilizes the Tweepy and Twitch-python libraries to access the Twitch and Twitter APIs. Checks Twitch once per minute to see if a live stream of a given user has started. If a stream is found, there is a 15 minute grace period to allow the streamer to send their own, more personal Tweet. This system is meant to function as a back up announcment if the streamer forgets. If no Tweet on the user's timeline is found to contain a link, the bot will Tweet an announcment with the stream link and title.
