# Single Responsibility Principle:
# 1. Ensure that a class has just a single instance
# 2. Provide a global access point to that instance

class MyClass(object):
    __instance = None
    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super(MyClass, cls).__new__(cls)
            cls.__instance.__initialized = False
        return cls.__instance

    def __init__(self):
        if (self.__initialized): return
        print("Initializing.....")
        self.__initialized = True

    
if __name__ == "__main__":
    myClass = MyClass()
    myClass_new = MyClass()
    if id(myClass) == id(myClass_new):
        print("Singleton works, both variables contain the same instance.")
    else:
        print("Singleton failed, variables contain different instances.")