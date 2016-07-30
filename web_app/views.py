from web_app.api_adapter import api_adapter
from flask import render_template, request
from web_app.crawler.crawler import crawler
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
    url = restaurants[0].url
    name = restaurants[0].name
    worker = crawler()
    images = worker.get_images(url)
    return render_template('result_test.html', images=images, name=name)

# api test page
@app.route("/test/<string:location>/<string:cata>")
def test_get(location, cata):
    adapter = api_adapter.API_adapter()
    restaurants = adapter.get_restaurant(location=location, category_filter=cata)
    restaurants = [i.name for i in restaurants]
    return str(restaurants)

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