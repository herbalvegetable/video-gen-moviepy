import os
import json
from praw import Reddit
from dotenv import load_dotenv
load_dotenv()

reddit = Reddit(
    client_id=os.environ['REDDIT_API_CLIENT_ID'],
    client_secret=os.environ['REDDIT_API_CLIENT_SECRET'],
    user_agent=f'my-app by {os.environ['REDDIT_API_USERNAME']}',
    username=os.environ['REDDIT_API_USERNAME'],
    password=os.environ['REDDIT_API_PASSWORD'],
)

