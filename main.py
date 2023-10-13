import os
from instagrapi import Client
from dotenv import load_dotenv
from utils import change_aspect_ratio


load_dotenv()

cl = Client()
cl.login(os.getenv('INSTAGRAM_USERNAME'), os.getenv('INSTAGRAM_PASSWORD'))

user_id = cl.user_id_from_username(os.getenv('INSTAGRAM_USERNAME'))

image_path = 'images/Pasted image.jpeg'
caption = 'content'

change_aspect_ratio(image_path)

cl.photo_upload(image_path, caption)

print('user_id', user_id)
