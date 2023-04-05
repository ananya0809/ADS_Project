from ride import Ride
from rbt_minheap import DictPair
from rbtree import RedBlackTree
from minheap import MinHeap
from input_output_handler import FileHandler
from input_output_handler import OperationType

handle = FileHandler()


operations = handle.parseFile()

print(operations)

# rides = [
#     Ride(25,98,46),
#     Ride(42,17,89),
#     Ride(9,76,31),
#     Ride(53,97,22),
#     Ride(68,41,51)
#     # Ride(27,17,88)
# ]

# dictionary = DictPair()

# # rbt = RedBlackTree(dictionary)
# minhp = MinHeap(10, dictionary)

# for ride in rides:
#     minhp.insert(ride)
#     # print(minhp.size)
#     # dictionary.printAll()
# minhp.minHeap()
# dictionary.printAll()
# for _ in range(0,5):
#     dictionary.printAll()
#     print(minhp.remove().to_str())
#     minhp.minHeap()
#     print("________________")
    

# print(minhp.size)
# minhp.Print()

    # minhp.insert(ride)

# print(minhp.Search(rides[3]))


# def getIndex(rideNumber):
#     searchRide = rbt.search(rideNumber)
#     ind = DictPair.rbtIndex(searchRide)
#     print(ind)


# for index in range(0, len(rides)):
#     print(rides[index].to_str())
#     if rides[index+1].rideNumber != rides[index].rideNumber:
#         break
    
    # print(rides[index].rideNumber, rides[index+1].rideNumber)
