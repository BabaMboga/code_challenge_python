from Article import Article

class Author:
    #Author initialised with name as a string
    def __init__(self,name):
        self.name = name
        self.articles_list = []
    #name cannot be changed after initialisation

    #returns the name of the author
    def name(self):
        return self.name
    
    #returns a list of article instances the author has written 
    def articles(self):
        return self._articles
    
    def magazines(self):
        unique_mag = set()
        for article in self.articles_list:
            unique_mag.add(article.magazine)

        return list(unique_mag)
    
    def add_article(self, magazine, title):
        article = Article(self, magazine, title)
        self._articles.append(article)

    def topic_areas(self):
        return list({article.magazine().category() for article in self._articles})
