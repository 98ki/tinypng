from __future__ import absolute_import
from tinypng.tinypng import TinyPng
import requests


client = TinyPng(api_key="YOUR_API_KEY")
image = requests.get("http://docs.python-requests.org/en/latest/_static/requests-sidebar.png").content
try:
    resp = client.shrink(data=image)
    print("Compressed file can be found at: {}".format(resp.headers.get("location")))

except Exception as e:
    print(e.message)
