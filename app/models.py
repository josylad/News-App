class News:
    '''
    News class to define News Objects
    '''
    def __init__(self,url, id, name, description, category):
        self.url=url
        self.id=id
        self.name=name
        self.description=description
        self.category=category


class NewsArticles:
    '''
    News Articles class to define MArticles Objects
    '''
    def __init__(self,url, id, name, description, author, title, urlToImage, time):
        self.url=url
        self.id=id
        self.name=name
        self.description=description
        self.author =author
        self.title=title
        self.urlToImage= urlToImage
        self.time=time
        
        