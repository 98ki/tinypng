from __future__ import print_function, absolute_import
import requests
from tinypng.settings import api_hash, api_url


class TinyPng(object):
    def __init__(self, api_key=None, sandbox=False):
        """
        :param api_key: your TinyPNG API key; sign up for a developer API key at http://tinypng.com/developers
        :return: An instance of a TinyPNG client
        """
        if api_key is None:
            raise Exception("Please provide a valid API key from TinyPNG. "
                            "You can sign up at http://tinypng.com/developers")

        self.api_key = api_key
        self.api_url = api_url["base"] if not sandbox else api_url["sandbox"]

    def __getattr__(self, method_call):

        def make_call(self, **kwargs):
            if method_call not in api_hash:
                raise AttributeError("Unsupported API method")
            api_fn = api_hash[method_call]

            base_url = self.api_url + api_fn["url"]
            method = api_fn["method"].lower()
            req_kwargs = {
                "params": kwargs.get("params", {}),
                "data": kwargs.get("data", {}),
                "headers": kwargs.get("headers", {}),
                "verify": False,  # avoid SSL
                "auth": ("api", self.api_key)  # Basic Auth
            }
            response = getattr(requests, method)(base_url, **req_kwargs)
            response.connection.close()

            if 200 <= response.status_code < 300:
                setattr(response, 'json', response.json())
                setattr(response, 'status', response.status_code)
                return response

            else:
                raise Exception("non valid response. Error: {error} - {message}".format(**response.json()))

        return make_call.__get__(self)
