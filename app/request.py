from config import Config
import requests
import json
from .models import News, NewsArticles 



API_KEY =Config.API_KEY

def get_sources():
    sources_list = []
    sources_url = 'https://newsapi.org/v2/sources?language=en&apiKey={}'.format(API_KEY)
    response = requests.get(sources_url)
    if response.status_code == 200:
        response_json =  response.json()
        sources = response_json['sources']
        for data in sources:
            url = data.get('url')
            id = data.get('id')
            name = data.get('name')
            description =  data.get('description')
            category = data.get('category')
            news_obj = News(url,id,name,description,category)
            sources_list.append(news_obj)
        print(sources)
        return sources


def get_news(id):
    print("***********************************")
    print("I am getting the news article")    
    news_list = []
    articles_url = 'https://newsapi.org/v2/top-headlines?sources={}&apiKey={}'.format(id, API_KEY)
    response = requests.get(articles_url)
    if response.status_code == 200:
        response_json =  response.json()
        
        articles = response_json['articles']
        
        for data in articles:
            url = data.get('url')
            id = data.get('id')
            source = data.get('source')
            name = source.get('name')
            title = data.get('title')
            description =  data.get('description')
            author = data.get('author')
            time = data.get('publishedAt')
            urlToImage = data.get('urlToImage')

            news_article = NewsArticles(url, id, name, description, author, title, urlToImage,time)
            news_list.append(news_article)
            print("***********************************")
            print(name)
            print("***********************************")
        
        return news_list
    


def get_article(self, article):
    pass


