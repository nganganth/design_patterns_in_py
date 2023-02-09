# a Director Class
from house_builder import HouseBuilder

class WestDirector:
    @staticmethod
    def construct():
        return HouseBuilder()\
            .set_building_type("WestDirector")\
            .set_number_windows(100)\
            .set_number_doors(20)\
            .set_wall_material("Wood")\
            .get_result()
    
