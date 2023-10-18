import os
from instagrapi import Client
from dotenv import load_dotenv
from utils import change_aspect_ratio
import requests


load_dotenv()

# post on instagram
cl = Client()
cl.login(os.getenv('INSTAGRAM_USERNAME'), os.getenv('INSTAGRAM_PASSWORD'))

user_id = cl.user_id_from_username(os.getenv('INSTAGRAM_USERNAME'))

image_path = 'images/Pasted image.jpeg'
caption = 'content'

change_aspect_ratio(image_path)

cl.photo_upload(image_path, caption)

print('user_id', user_id)

# post on linkedin
profile_id = 'YOUR_PROFILE_ID'

#scope: w_member_social,r_liteprofile
access_token = 'YOUR_ACCESS_TOKEN'

url = "https://api.linkedin.com/v2/ugcPosts"

headers = {'Content-Type': 'application/json',
           'X-Restli-Protocol-Version': '2.0.0',
           'Authorization': 'Bearer ' + access_token}


post_data = {
    "author": "urn:li:person:"+profile_id,
    "lifecycleState": "PUBLISHED",
    "specificContent": {
        "com.linkedin.ugc.ShareContent": {
            "shareCommentary": {
                "text": "Hello World! This is my first Share on LinkedIn!!"
            },
            "shareMediaCategory": "NONE"
        }
    },
    "visibility": {
        "com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"
    }
}

response = requests.post(url, headers=headers, json=post_data)

print(response)
