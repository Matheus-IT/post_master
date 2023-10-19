import os
import json
from instagrapi import Client
from dotenv import load_dotenv
from utils import change_aspect_ratio, env
import requests
from icecream import ic


load_dotenv()

# # post on instagram
# cl = Client()
# cl.login(os.getenv('INSTAGRAM_USERNAME'), os.getenv('INSTAGRAM_PASSWORD'))

# user_id = cl.user_id_from_username(os.getenv('INSTAGRAM_USERNAME'))

# image_path = 'images/Pasted image.jpeg'
# caption = 'content'

# change_aspect_ratio(image_path)

# cl.photo_upload(image_path, caption)

# print('user_id', user_id)

# =============================================================================
# # post on linkedin
# profile_id = os.getenv('LINKEDIN_PROFILE_ID')

# #scope: w_member_social,r_liteprofile
# access_token = os.getenv('LINKEDIN_ACCESS_TOKEN')

# url = "https://api.linkedin.com/v2/ugcPosts"

# headers = {'Content-Type': 'application/json',
#            'X-Restli-Protocol-Version': '2.0.0',
#            'Authorization': 'Bearer ' + access_token}


# post_data = {
#     "author": "urn:li:person:"+profile_id,
#     "lifecycleState": "PUBLISHED",
#     "specificContent": {
#         "com.linkedin.ugc.ShareContent": {
#             "shareCommentary": {
#                 "text": "Hello World! This post was made with python!"
#             },
#             "shareMediaCategory": "NONE"
#         }
#     },
#     "visibility": {
#         "com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"
#     }
# }

# response = requests.post(url, headers=headers, json=post_data)

# ic(response)
# =============================================================================
import requests

# Replace with your Facebook App credentials
app_id = env('FACEBOOK_APP_ID')
app_secret = env('FACEBOOK_APP_SECRET')
access_token = env('FACEBOOK_ACCESS_TOKEN')

# The page or user ID where you want to post
page_id = env('FACEBOOK_USER_ID')

# Post data
post_data = {
    'message': 'Hello world!',
    'access_token': access_token
}

# Make the post request
url = f'https://graph.facebook.com/{page_id}/feed'
response = requests.post(url, data=post_data)

if response.status_code == 200:
    ic('Post successful!')
else:
    ic('Post failed. Status code:', response.status_code, json.loads(response.content))
