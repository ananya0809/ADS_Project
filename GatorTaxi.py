# import
from rbtree import RedBlackTree
from minheap import MinHeap
from ride import Ride
from rbt_minheap import DictPair
from input_output_handler import FileHandler
from input_output_handler import OperationType

# insert


# def Pointers(allrides):
#         for ride in range(0, len(allrides)):
#             dictionary.key = ride
#             dictionary.value = {rbt.search()}
#             dictionary.put(dictionary.key, dictionary.value)



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
    print(minhp.size)

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

# Operation 5
def CancelRide(rideNumber):
    toDelete = rbt.search(rideNumber)
    if toDelete != None:
        rbt.delete(toDelete)
    

# Dictionary for Pointers between MinHeap and Red Black Tree
dictionary = DictPair()

# init
rbt = RedBlackTree(dictionary)
minhp = MinHeap(100, dictionary)

# File Handling between Input and Output file
operations = FileHandler().parseFile()

# print(operations)

for operation in operations:
    if operation[0] == OperationType.INSERT:
        insert_ride(operation[1], operation[2], operation[3])
    if operation[0] == OperationType.GETNEXTRIDE:
        print(GetNextRide().to_str())

# print(print_ridenum(9).ride.to_str())
# print_ride1_ride2(4, 31)
# print(GetNextRide().to_str())

