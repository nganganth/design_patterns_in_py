from prototype import Prototype
import time
import copy

class DramaBook(Prototype):
    def __init__(self, title, author, pages, publisher, copies):
        super().__init__()
        time.sleep(3)
        self.title = title
        self.author = author
        self.pages = pages
        self.publisher = publisher
        self.copies = copies
        self.language = {"ENG", "JP"}
    
    def clone(self):
        return copy.deepcopy(self)