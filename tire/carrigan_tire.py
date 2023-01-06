
from tire.tire import Tire

class CarriganTire(Tire):

    def __init__(self, tire_wear_array = [0.0,0.0,0.0,0.0]):
        self.tire_wear_array = tire_wear_array
    
    def needs_service(self) -> bool:
        i = 0
        while i < 4:
            if self.tire_wear_array[i] >= 0.9:
                return True
            i += 1
    



        