from yelp.oauth1_authenticator import Oauth1Authenticator
from yelp.client import Client
from random import randint
import json
import io
import os, sys

class API_adapter(object):

    def __init__(self):
        '''
        Load Oauth keys
        '''
        _path_ = os.path.abspath(os.path.dirname(sys.argv[0]))
        _path_ = '/'.join([_path_,'web_app/api_adapter/config_secret.json'])
        cred = io.open(_path_)
        cred = json.load(cred)  
        auth = Oauth1Authenticator(**cred)
        self.client = Client(auth)

    def get_restaurant(self, location, category_filter=None):
        params = {
            'term': 'food',
            'location': location,
            'cc' : 'US'
        }
        if category_filter:
            params['category_filter'] = category_filter

        restaurant = self.client.search(**params)
        return restaurant.businesses

