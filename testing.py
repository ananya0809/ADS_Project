from rbt_minheap import DictPair

class Testing1:

    def __init__(self, mydict):
        self.mydict = mydict
        print("setting up class")

    def setup(self, k, v1, v2):
        self.mydict.put(k, v1, v2)
        # self.a = 123

dictionary = DictPair()
dictionary.put(1, 2, 3)
dictionary.printAll()

# thisdict = {
#     "key": "initial"
# }
testing_obj = Testing1(dictionary)

# print()
testing_obj.setup(4, 5, 6)
dictionary.printAll()

# print(testing_obj.a)
# testing_obj.setup()
# print(testing_obj.a)

