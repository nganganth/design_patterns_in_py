from prototype import Prototype
import copy
import time

class NonfictionBook(Prototype):
    def __init__(self, title, author, pages, publisher, copies):
        self.edition = 2
    
    def clone(self):
        return copy.deepcopy(self)