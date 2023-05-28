class Article:
    articles_list = []

    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        self.articles_list.append(self)

    #return the title for that given article
    def title(self):
        return self.title
    
    #returns a list of all article instances
    @classmethod
    def all(cls):
        return cls.articles_list
    
    #returns the author for that given article
    def author(self):
        return self._author
    
    #returns the magazine for that given article
    def magazine(self):
        return self._magazine
