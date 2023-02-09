# a Director Class
from house_builder import HouseBuilder

class NorthDirector:
    @staticmethod
    def construct():
        return HouseBuilder()\
            .set_building_type("NorthDirector")\
            .set_number_windows(8)\
            .set_number_doors(2)\
            .set_wall_material("Ice")\
            .get_result()
    
