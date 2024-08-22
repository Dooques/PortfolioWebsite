import requests
import os
import json


def get_posts():
    api_key = os.environ.get('api_key')
    params = {'key': api_key}
    blog_id = '2697739541772529687'
    blog_uri = f'https://www.googleapis.com/blogger/v3/blogs/{blog_id}/posts'
    response = requests.get(blog_uri, params)
    return response.json()


posts = get_posts()
with open('files/post_data.json', 'w') as json_file:
    json.dump(posts, json_file, indent=4)
