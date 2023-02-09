from prototype import Prototype
import time
import copy

class FictionBook(Prototype):
    def __init__(self, title, author, pages, publisher, copies):
        self.price = 10
    
    def clone(self):
        return copy.deepcopy(self)