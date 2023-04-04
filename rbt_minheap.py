class DictPair(dict):

    rbtIndex: int
    minhpIndex: int

    def __init__(self):
        self = dict()
    
    def put(self, key, rbtInd, minhpInd):
        self[key] = {rbtInd, minhpInd}
    



