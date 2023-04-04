class DictPair(dict):

    rbtIndex: int
    minhpIndex: int

    def __init__(self):
        self.dict = dict()
    
    def put(self, key, rbtInd, minhpInd):
        self.dict[key] = (rbtInd, minhpInd)
    
    def get(self, key):
        try:
            return self.dict[key]
        except:
            self.put(key, -1, -1)
            return self.get(key)

    def printAll(self):
        print (self.dict)
    



