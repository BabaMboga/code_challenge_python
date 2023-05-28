class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category

    #name can be changed
    def set_name(self, new_name):
        self._name = new_name

    #returns name of the magazine
    def name(self):
        return self._name
    
    #returns category
    def category(self):
        return self._category