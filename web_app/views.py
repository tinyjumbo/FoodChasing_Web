from web_app.api_adapter import api_adapter
from web_app.crawler.crawler import crawler
from flask import render_template, request
from random import randint
from . import app
import json

# index page
@app.route("/")
def show_index_page():
    return render_template('index.html')

# result page
@app.route("/result", methods=['GET'])
def show_random():
    location = request.args.get('location')
    cata = request.args.get('cata')
    adapter = api_adapter.API_adapter()
    restaurants = adapter.get_restaurant(location=location, category_filter=cata)
    # pick a random restaurant
    index = randint(0,len(restaurants)-1)
    restaurants = restaurants[index]
    name = restaurants.name
    url = restaurants.url
    addr = ', '.join(restaurants.location.display_address)
    worker = crawler()
    images = worker.get_images(url)
    return render_template('result_test.html', images=images, name=name, url=url, addr=addr)

# api test page
@app.route("/test/<string:location>/<string:cata>")
def test_get(location, cata):
    adapter = api_adapter.API_adapter()
    restaurants = adapter.get_restaurant(location=location, category_filter=cata)
    #restaurants = [i.name for i in restaurants]
    restaurants = restaurants[0] 
    return str(', '.join(restaurants.location.display_address))

# save my favorite
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