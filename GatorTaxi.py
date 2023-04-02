from rbtree import RedBlackTree
import heapq
from ride import Ride
from minheap import MinHeap

# init
bst = RedBlackTree()

# insert
bst.insert(Ride(5, 0, 0))  # inserts a node with value 5
bst.insert(Ride(7,0,0))
bst.insert(Ride(3,0,0))
bst.insert(Ride(9,0,0))

# bst.delete(Ride(5, 0, 0))

bst.print_tree()

print(bst.minimum().ride.rideNumber)
# bst.delete(3)
# print(bst.minimum())
# print(bst.minimum())

# define ride class
