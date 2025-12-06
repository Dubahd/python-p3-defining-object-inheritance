# Import the Vehicle class
from vehicle import Vehicle

class Car(Vehicle):
    # No need to redefine __init__ - it inherits from Vehicle
    
    def go(self):
        return "VRRROOOOOOOOOOOOOOOOOOOOOOOM!!!!!"