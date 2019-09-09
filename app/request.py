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


