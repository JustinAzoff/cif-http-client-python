"""
Client for the CIF HTTP API

https://code.google.com/p/collective-intelligence-framework/wiki/API_v1#HTTP
"""

import requests
import json

class Client:
    def __init__(self, url, api_key, http_opts={}, **default_params):
        """
        :param url: URL of CIF API endpoint
        :param api_key: CIF API key
        :param http_opts: Extra options to add to requests.session

        Any Extra kwargs will be passed on to search
        """
        self.url = url
        self.api_key = api_key

        self.session = requests.session()
        self.session.headers["Accept"] = "application/json"
        for k,v in http_opts.items():
            setattr(self.session, k, v)

        self.default_params = default_params
        self.default_params["apikey"] = api_key

    def search(self, **kwargs):
        """
        Search CIF Data.  Accepted Options:
        :param confidence: filter by confidence, [0-100]
        :type confidence: int
        :param restriction: filter by restriction, [public|need-to-know|private]
        :param guid: filter by group uuid
        :param nomap: don't map restriction to your local restriction map
        :type nomap: bool
        :param nolog: Don't log the query
        :type nolog: bool
        """
        params = kwargs
        params.update(self.default_params)
        body = self.session.get(self.url, params=params).text
        data = [json.loads(line) for line in body.splitlines()]
        return data
