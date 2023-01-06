
from tire.tire import Tire

class OctoprimeTire(Tire):

    def __init__(self, tire_wear_array = [0.0,0.0,0.0,0.0]):
        self.tire_wear_array = tire_wear_array
    
    def needs_service(self) -> bool:
        if sum(self.tire_wear_array) >= 3:
            return True