from flask import render_template, request
from . import app
from web_app.api_adapter import api_adapter
import json

# index page
@app.route("/")
def show_index_page():
    return render_template('index.html')

# api test page
@app.route("/test/<string:location>/<string:cata>")
def test_get(location, cata):
    adapter = api_adapter.API_adapter()
    restaurants = adapter.get_restaurant(location=location, category_filter=cata)
    restaurants = [i.name for i in restaurants]
    return str(restaurants)



@app.route("/save/favorite", methods=['post'])
def test_post():
    '''
    To be implemented with DB connection
    '''
    print(request.json)
    return("Success!")



"""
curl -i http://127.0.0.1:5000/{location}/{food_cata}

curl -i -H "Content-Type: application/json" -X POST -d '{"title":"Read a book"}' http://127.0.0.1:5000/save/favorite

http://blog.miguelgrinberg.com/post/designing-a-restful-api-with-python-and-flask
"""