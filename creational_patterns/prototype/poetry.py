from prototype import Prototype
import time
import copy

class PoetryBook(Prototype):
    def __init__(self, title, author, pages, publisher, copies):
        self.language = {"ENG"}
    
    def clone(self):
        return copy.deepcopy(self)