from flask import render_template
from . import app

# index page
@app.route("/")
def show_index():
    return render_template('index.html')