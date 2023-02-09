from drama import DramaBook
from fiction import FictionBook
from nonfiction import NonfictionBook
from poetry import PoetryBook
import datetime

if __name__ == '__main__':
    ## This will take time for creating new DramaBook ##
    print(f"Started Instantiating DramaBook {datetime.datetime.now().time()}")
    for i in range(10):
        dramabook = DramaBook("Then she was gone", "Lisa Jewell", 500, "Simon & Schuster", 1000)
        print(f"Finished creating DramaBook {datetime.datetime.now().time()}")
    # print("Attributes " + ", ".join("%s : %s " % item for item in vars(dramabook).items()))
    print(f"Started Instantiating DramaBook {datetime.datetime.now().time()}")

    ## This will run faster ## 
    print(f"Started Instantiating DramaBook {datetime.datetime.now().time()}")
    dramabook_template = DramaBook("Then she was gone", "Lisa Jewell", 500, "Simon & Schuster", 1000)
    fictionbook_template = FictionBook("Harry Potter", "J. K. Rowling", 9230000, "Bloomsbury", 413704)
    nonfictionbook_template = NonfictionBook("Atomic Habits", "James Clear", 29742, "Penguin Random House", 7532)
    poetrybook_template = PoetryBook("Not found", "Not found", 0, "Not found", 0)
    for i in range(500):
        dramabook = dramabook_template.clone()
        fictionbook = fictionbook_template.clone()
        nonfictionbook = nonfictionbook_template.clone()
        poetrybook = poetrybook_template.clone()
        print(f"Finished creating DramaBook {datetime.datetime.now().time()}")
    print(f"Started Instantiating DramaBook {datetime.datetime.now().time()}")

