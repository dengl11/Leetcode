from collections import OrderedDict
class LRUCache:

    def __init__(self, capacity: int):
        self.data = OrderedDict()
        self.c = capacity
        

    def get(self, key: int) -> int:
        if key not in self.data: return -1
        v = self.data.pop(key)
        self.data[key] = v
        return v
        

    def put(self, key: int, value: int) -> None:
        if key not in self.data and self.c < len(self.data) + 1:
            self.data.popitem(last = False)
        self.get(key)
        self.data[key] = value
        