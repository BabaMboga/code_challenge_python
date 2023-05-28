class Magazine:
    magazines_list = []

    def __init__(self, name, category):
        self.name = name
        self.category = category
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