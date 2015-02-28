from __future__ import absolute_import
from tinypng.tinypng import TinyPng
import requests


client = TinyPng(api_key="YOUR_API_KEY")
url = "http://docs.python-requests.org/en/latest/_static/requests-sidebar.png"
try:
    resp = client.shrink(data=requests.get(url).content)
    print("Compressed file can be found at: {}".format(resp.headers.get("location")))

except Exception as e:
    print(e.message)
