import tweepy
import time
import hn_n_lidovky
import irozhlas_seznam_ct24 

#udaje
api_key = :)
api_secret = :)

access_token = :)
access_token_secret = :)

#login
auth = tweepy.OAuthHandler(api_key, api_secret)
auth.set_access_token(access_token,access_token_secret)
api = tweepy.API(auth)

def Tweet1():
	tweet1 = irozhlas_seznam_ct24.irozhlas() + "\n" + irozhlas_seznam_ct24.seznam() + "\n" + irozhlas_seznam_ct24.ct24()
	delka1 = len(tweet1)
	rozdil1 = 280 - delka1
	if rozdil1 < 0:
		novy_tweet1 = tweet1[:(rozdil1-3)] + "..." 
		api.update_status(novy_tweet1)
	else:	
		api.update_status(tweet1)
					

def Tweet2():
	tweet2 = hn_n_lidovky.HN() + "\n" + hn_n_lidovky.DenikN() + "\n" + hn_n_lidovky.Lidovky()
	delka2 = len(tweet2)
	rozdil2 = 280 - delka2
	if rozdil2 < 0:
		novy_tweet2 = tweet2[:(rozdil2-3)] + "..." 
		api.update_status(novy_tweet2)
	else:	
		api.update_status(tweet2)
						

if ((time.localtime()[3] >= 6) and (time.localtime()[3] <= 21)):
	try: 
		Tweet1()
	finally:
		Tweet2()
	time.sleep(10800)
else:
	time.sleep(1800)
