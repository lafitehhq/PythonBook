from twitter import Twitter

# Todo:翻墙调试
#Make sure to add the access tokens and consumer keys for your application
t = Twitter(auth=("Access Token", "Access Token Secret", "Consumer Key", "Consumer Secret"))
pythonTweets = t.search.tweets(q="#python")
print(pythonTweets)