# Python3 implementation of Min Heap

import sys
from ride import Ride
from rbt_minheap import DictPair


class MinHeap:
    def __init__(self, maxsize, dictionary: DictPair):
        self.maxsize = maxsize
        self.size = 0
        self.Heap = [Ride(0, 0, 0)] * (self.maxsize + 1)
        self.Heap[0] = Ride(0, -1 * sys.maxsize, 0)
        self.FRONT = 1
        self.dictionary = dictionary

    # Function to return the position of
    # parent for the node currently
    # at pos
    def parent(self, pos):
        return pos // 2

    # Function to return the position of
    # the left child for the node currently
    # at pos
    def leftChild(self, pos):
        return 2 * pos

    # Function to return the position of
    # the right child for the node currently
    # at pos
    def rightChild(self, pos):
        return (2 * pos) + 1

    # Function that returns true if the passed
    # node is a leaf node
    def isLeaf(self, pos):
        return pos * 2 > self.size

    # Function to swap two nodes of the heap
    def swap(self, fpos, spos):
        self.Heap[fpos], self.Heap[spos] = self.Heap[spos], self.Heap[fpos]

    # Function to heapify the node at pos
    def minHeapify(self, pos):

        # If the node is a non-leaf node and greater
        # than any of its child
        if not self.isLeaf(pos):
            if (
                self.Heap[pos].rideCost > self.Heap[self.leftChild(pos)].rideCost
                or self.Heap[pos].rideCost > self.Heap[self.rightChild(pos)].rideCost
            ):

                # Swap with the left child and heapify
                # the left child
                if (
                    self.Heap[self.leftChild(pos)].rideCost
                    < self.Heap[self.rightChild(pos)].rideCost
                ):
                    self.swap(pos, self.leftChild(pos))
                    self.minHeapify(self.leftChild(pos))

                # Swap with the right child and heapify
                # the right child
                else:
                    self.swap(pos, self.rightChild(pos))
                    self.minHeapify(self.rightChild(pos))
        ride_pointer = self.dictionary.get(self.Heap[pos].rideNumber)
        result = self.Search(self.Heap[pos])
        self.dictionary.put(self.Heap[pos].rideNumber, ride_pointer[0], result)

    # Function to insert a node into the heap
    def insert(self, ride: Ride):
        if self.size >= self.maxsize:
            return
        self.size += 1
        self.Heap[self.size] = ride

        current = self.size

        while self.Heap[current].rideCost < self.Heap[self.parent(current)].rideCost:
            self.swap(current, self.parent(current))
            current = self.parent(current)
        ride_pointer = self.dictionary.get(ride.rideNumber)
        result = self.Search(ride)
        self.dictionary.put(ride.rideNumber, ride_pointer[0], result)

    # Function to print the contents of the heap
    def Print(self):
        for i in range(1, (self.size // 2) + 1):
            print(
                " PARENT : "
                + str(self.Heap[i].rideCost)
                + " LEFT CHILD : "
                + str(self.Heap[2 * i].rideCost)
                + " RIGHT CHILD : "
                + str(self.Heap[2 * i + 1].rideCost)
            )

    # Function to build the min heap using
    # the minHeapify function
    def minHeap(self):
        for pos in range(self.size // 2, 0, -1):
            self.minHeapify(pos)

    # Function to remove and return the minimum
    # element from the heap
    def remove(self):
        if self.size == 0:
            return Ride(0, 0, 0)
        popped = self.Heap[self.FRONT]
        ride_pointer = self.dictionary.get(popped.rideNumber)
        self.dictionary.put(popped.rideNumber, ride_pointer[0], -1)
        self.Heap[self.FRONT] = self.Heap[self.size]
        self.size -= 1
        self.minHeapify(self.FRONT)
        if self.size == 0:
            self.Heap = [Ride(0, 0, 0)] * (self.maxsize + 1)
            self.Heap[0] = Ride(0, -1 * sys.maxsize, 0)
            self.FRONT = 1
        return popped

    #  Function to search a ride in Heap
    def Search(self, ride):
        if self.size == 1 and self.Heap[1] == ride:
            return 1
        for i in range(1, (self.size // 2) + 1):
            if self.Heap[i] == ride:
                return i
            elif self.Heap[2 * i] == ride:
                return 2 * i
            elif self.Heap[2 * i + 1] == ride:
                return 2 * i + 1
        return -1


# Driver Code
# if __name__ == "__main__":

#     print("The minHeap is ")
#     minHeap = MinHeap(15)
#     minHeap.insert(Ride(0, 15, 0))
#     minHeap.insert(Ride(0, 10, 0))
#     minHeap.insert(Ride(0, 17, 0))
#     minHeap.insert(Ride(0, 10, 0))
#     minHeap.insert(Ride(0, 84, 0))
#     minHeap.insert(Ride(0, 19, 0))
#     minHeap.insert(Ride(0, 6, 0))
#     minHeap.insert(Ride(0, 22, 0))
#     minHeap.insert(Ride(0, 9, 0))
#     minHeap.minHeap()

#     minHeap.Print()
#     print("The Min val is " + str(minHeap.remove().rideCost))
