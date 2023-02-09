# a Director Class
from house_builder import HouseBuilder

class SouthDirector:
    @staticmethod
    def construct():
        return HouseBuilder()\
            .set_building_type("SouthDirector")\
            .set_number_windows(4)\
            .set_number_doors(1)\
            .set_wall_material("Sandstone")\
            .get_result()
    
