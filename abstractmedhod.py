class Base(object):
    #Abstractmethods
    def parse(self,query):
        raise NotImplementedError
        
        
#class method for facotry pattern
class Fridge(object):
    def __init__(self):
        self.cheese = 'chees'
        self.veg = "veg"

    def get_cheese(self):
        return self.cheese

    def get_vegetables(self):
        return self.veg


class Pizza(object):
    def __init__(self, ingredients):
        self.ingredients = ingredients

    @classmethod
    def from_fridge(cls, fridge):
        return cls(fridge.get_cheese() + fridge.get_vegetables())
