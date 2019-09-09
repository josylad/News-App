from flask import render_template, request, redirect, url_for
from . import main
from ..request import get_sources, get_news
from ..models import News


# Views
@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    sources = get_sources()
    return render_template("index.html", sources = sources ,error="Error while making request")



@main.route('/newspage/<id>')
def newspage(id):

    '''
    View news page function that returns the news details page and its data
    '''
    newspages = get_news(id)
    # title = name
    
    return render_template('newspage.html', newspages=newspages)


