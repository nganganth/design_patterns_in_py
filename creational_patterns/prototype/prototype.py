import time
from abc import ABC, abstractmethod

class Prototype(ABC):
    def __init__(self):
        time.sleep(3)
        self.title = None
        self.author = None
        self.pages = None
        self.publisher = None
        self.copies = None
    
    @abstractmethod
    def clone(self):
        pass