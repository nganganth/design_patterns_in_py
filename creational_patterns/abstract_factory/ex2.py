from __future__ import annotations
from abc import ABC, abstractmethod

class Browser(ABC):
    @abstractmethod
    def create_search_toolbar(self):
        pass

    @abstractmethod
    def create_browser_window(self):
        pass

class Messenger(ABC):
    @abstractmethod
    def create_messenger_window(self):
        pass

class NormalBrowser(Browser):
    def create_search_toolbar(self):
        print("NormalBrowser - Search Toolbar is created")
    
    def create_browser_window(self):
        print("NormalBrowser - Browser Window is created")

class NormalMessenger(Messenger):
    def create_messenger_window(self):
        print("NormalMessenger - Messenger Window is created")

class SecureBrowser(Browser):
    def create_search_toolbar(self):
        print("SecureBrowser - Search Toolbar is created")
    
    def create_browser_window(self):
        print("SecureBrowser - Browser Window is created")
    
    def create_incognito_mode(self):
        print("SecureBrowser - Incognito Mode is created")

class SecureMessenger(Messenger):
    def create_messenger_window(self):
        print("SecureMessenger - Messenger Window is created")
    
    def create_privacy_filter(self):
        print("SecureMessenger - Privacy Filter is created")
    
    def disappearing_messages(self):
        print("SecureMessenger - Disappearing Messages Feature Enabled")

class AbstractFactory(ABC):
    @abstractmethod
    def create_browser(self):
        pass

    @abstractmethod
    def create_messenger(self):
        pass

class NormalProductFactory(AbstractFactory):
    def create_browser(self):
        return NormalBrowser()
    def create_messenger(self):
        return NormalMessenger()

class SecureProductFactory(AbstractFactory):
    def create_browser(self):
        return SecureBrowser()
    def create_messenger(self):
        return SecureMessenger()

if __name__ == '__main__':
    for factory in (NormalProductFactory(), SecureProductFactory()):
        product_a = factory.create_browser()
        product_b = factory.create_messenger()

        product_a.create_browser_window()
        product_a.create_search_toolbar()
        
        product_b.create_messenger_window()


