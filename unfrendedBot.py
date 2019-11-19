# bot to unfollow unpopular accounts that unfollowed you first

import tweepy as tp

# your api info
api_key = ''
api_secret = ''
access_token = ''
access_secret = ''

# login to twitter api
auth = tp.OAuthHandler(api_key,api_secret)
auth.set_access_token(access_token,access_secret)
api = tp.API(auth)


# Function that returns the differences between follower arrays
def diff(arr1, arr2):
    return list(set(arr1) - set(arr2))


you_follow = api.friends_ids()  # accounts that you follow
follow_you = api.followers_ids()  # accounts that follow you
you = api.me().id # your account

not_follow_me = diff(you_follow, follow_you) # list of accounts that you follow but don't follow you back

for id in not_follow_me:
    account = api.get_user(id)
    if account.followers_count < 200:  # condition to check if account is "popular" or not
       api.destroy_friendship(id)  # unfollow small account
