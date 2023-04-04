# import
from rbtree import RedBlackTree
from minheap import MinHeap
from ride import Ride
from rbt_minheap import DictPair

# init
rbt = RedBlackTree()
minhp = MinHeap(2000)

# insert
rides = [
    Ride(25,98,46),
    Ride(42,17,89),
    Ride(9,76,31),
    Ride(53,97,22),
    Ride(68,41,51)
    # Ride(27,17,88)
]

for ride in rides:
    rbt.insert(ride)
    minhp.insert(ride)

# Dictionary for Pointers between MinHeap and Red Black Tree
dictionary = DictPair()
def Pointers(allrides):
        for ride in range(0, len(allrides)):
            dictionary.key = ride
            dictionary.value = {rbt.search()}
            dictionary.put(dictionary.key, dictionary.value)



# Operation 1
def print_ridenum(rideNumber):
    searchRide = rbt.search(rideNumber)
    if type(searchRide.ride) == Ride:
        print (searchRide.ride.to_str())

# Operation 2
def print_ride1_ride2(rideNumber1, rideNumber2):
    for rx in range(rideNumber1, rideNumber2):
        print_ridenum(rx)

# Operation 3
def insert_ride(rideNumber, rideCost, tripDuration):
    rbt.insert(Ride(rideNumber, rideCost, tripDuration))
    minhp.insert(Ride(rideNumber, rideCost, tripDuration))

# Operation 4
def GetNextRide():

    removedRides = []

    while True:
        tempRide = minhp.remove()
        if len(removedRides) > 0:
            if tempRide.rideCost == removedRides[0].rideCost:
                removedRides.append(tempRide)
            else:
                minhp.insert(tempRide)
                break
        else:
            removedRides.append(tempRide)

    minTrip = removedRides[0]
    for aRide in removedRides:
        if aRide.tripDuration < minTrip.tripDuration:
            minTrip = aRide
    
    removedRides.remove(minTrip)
    for remainingRides in removedRides:
        minhp.insert(remainingRides)

    return minTrip

    # print(minTrip.to_str())
    # print(aRide.to_str())

    # while minhp.size != 0:
    #     removeRide = minhp.remove()
    #     removedRides.append(removeRide)
    # for aRide in removedRides:
    #     print(aRide)
    #     if aRide.rideCost == (aRide+1).rideCost:
    #         if removedRides[index].tripDuration < removedRides[index+1].tripDuration:
    #             return aRide
    #         else:
    #             return (index+1)
    #     else:
    #         return aRide


    # tempRide = minhp.remove()

    # if removeRide.rideCost == tempRide.rideCost:
    #     if removeRide.tripDuration < tempRide.tripDuration:
    #         return removeRide
    #     else:
    #         return tempRide
    # else:
    #     return removeRide

# Operation 5
def CancelRide(rideNumber):
    toDelete = rbt.search(rideNumber)
    if toDelete != None:
        rbt.delete(toDelete)
    

# print(print_ridenum(9).ride.to_str())
# print_ride1_ride2(4, 31)
print(GetNextRide().to_str())

