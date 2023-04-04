class Ride:
    rideNumber: int
    rideCost: int
    tripDuration: int

    def __init__(self, rn, rc, td):
        self.rideNumber = rn
        self.rideCost = rc
        self.tripDuration = td
    
    def to_str(self):
        return str(self.rideNumber) + " " + str(self.rideCost) + " " + str(self.tripDuration)

        

