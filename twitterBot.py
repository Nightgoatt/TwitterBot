import tweepy
import time
import random
import multiprocessing


api_key = ''
secret_key = ''
access_token = ''
secret_token = ''

auth = tweepy.OAuthHandler(api_key, secret_key)
auth.set_access_token(access_token, secret_token)
api = tweepy.API(auth)


# Random like search by hashtags or words function.
def like():
 while True:
    sch = ['']
    query = random.choice(sch)
    limit = 1
    for tweet in tweepy.Cursor(api.search, q=query, result_type = 'mixed').items(limit):
        if not tweet.favorited:
            try:
                print('Searching...')
                time.sleep(2)
                if (tweet.user.followers_count > 600):
                 tweet.favorite()
                 print('Liked a tweet!\nPlease wait...')
                 time.sleep(60 * 5)
                else:
                    print('Error with user: ' + tweet.user.screen_name + '\nWaiting...')
                    time.sleep(10)
            except tweepy.TweepError as e:
                print(e.reason + '\nWaiting...')
                time.sleep(10)
            except StopIteration:
                break
            

# Retweet from user.
def retweet():
    while True:
        try:
         user = ['']
         query = random.choice(user)
         for tweet in tweepy.Cursor(api.search, q=query, count=1).items(1):
          if (tweet.user.followers_count > 3000):
              tweet.retweet()
              tweet.favorite()
              print('Liked and retweeted from: ' + tweet.user.screen_name + '\n\nWaiting...')
              time.sleep(30)
          else:
              print('Insuficient followers.')
              continue
        except tweepy.TweepError as e:
            print(e.reason + '\n\nWaiting...')
            time.sleep(10)
            continue
        


# Checks if a follower follows you and follows that user back.
def follow_followers():
    print("Searching for followers...")
    for follower in tweepy.Cursor(api.followers).items():
      if not follower.following:
        try:
          time.sleep(10)
          follower.follow()
          print(f"Following {follower.name}")
          time.sleep(60)
        except tweepy.TweepError as e:
           print(e.reason)
           continue

# Checks if a follower has more than 'x' number of followers and follows him.
def check_followers():
  while True:
   search = tweepy.Cursor(api.followers).items()
   for follower in search:
     if (follower.followers_count > 100):
         follow_followers()
     else:
         continue
   time.sleep(5 * 60)

f1 = multiprocessing.Process(target = like)
f2 = multiprocessing.Process(target = retweet)
f3 = multiprocessing.Process(target = check_followers)

if __name__ == '__main__':
     f1.start()
     f2.start()
     f3.start()