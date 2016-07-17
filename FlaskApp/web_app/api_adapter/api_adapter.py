from yelp.oauth1_authenticator import Oauth1Authenticator
from yelp.client import Client
import json
import io

# read API keys
with io.open('config_secret.json') as cred:
    creds = json.load(cred)
    auth = Oauth1Authenticator(**creds)
    client = Client(auth)

    params = {
        'term': 'food',
        'location': '02155',
        'cc' : 'US',
        'category_filter': 'chinese'
    }

    a = client.search(**params)

    b = [i.name for i in a.businesses]
    print(b)