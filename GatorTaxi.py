from rbtree import RedBlackTree
import heapq

# init
bst = RedBlackTree()

# insert
bst.insert(5)  # inserts a node with value 5
bst.insert(7)
bst.insert(3)
bst.insert(9)

# bst.delete(3)

bst.print_tree()

print(bst.minimum())
bst.delete(3)
print(bst.minimum())
print(bst.minimum())

# define ride class


