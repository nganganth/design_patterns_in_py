from north_director import NorthDirector
from south_director import SouthDirector
from west_director import WestDirector

if __name__ == '__main__':
    for director in (NorthDirector.construct(), 
                    SouthDirector.construct(),
                    WestDirector.construct()):
        print(director.construction())