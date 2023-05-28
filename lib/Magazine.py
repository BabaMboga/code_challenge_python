

class Magazine:
    magazines_list = []

    def __init__(self, name, category):
        self.name = name
        self.category = category
        self.articles = []
        self.magazines_list.append(self)

    #name can be changed
    def set_name(self, new_name):
        self._name = new_name

    #returns name of the magazine
    def name(self):
        return self._name
    
    #returns category
    def category(self):
        return self._category
    
    #returns a list of all magazine instances
    @classmethod
    def all(cls):
        return cls.magazines_list
    
    def contributors(self):
        return list({article.author() for article in self._articles})
    
    @classmethod
    def find_by_name(cls, name):
        for magazine in cls.magazines_list:
            if magazine.name() == name:
                return magazine
        return None
    
    @classmethod
    def article_titles(cls):
        return [article.title() for magazine in cls.magazines_list for article in magazine._articles]
    
    def contributing_authors(self):
        contributing_authors = []
        author_magazine_count = {}
        for article in self._articles:
            author = article.author()
            author_magazine_count[author] = author_magazine_count.get(author, 0) + 1
            if author_magazine_count[author] > 2 and author not in contributing_authors:
                contributing_authors.append(author)
        return contributing_authors