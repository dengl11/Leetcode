from collections import OrderedDict, defaultdict
class LFUCache:

    def __init__(self, capacity: int):
        self.vals = dict()
        self.keys = defaultdict(OrderedDict)
        self.minFreq = 1
        self.cap = capacity
        

    def get(self, key: int) -> int:
        if self.cap <= 0 or key not in self.vals: return -1
        val, freq = self.vals.pop(key)
        if self.minFreq == freq and len(self.keys[freq]) == 1:
            self.minFreq += 1
        self.keys[freq].pop(key)
        freq += 1
        self.keys[freq][key] = None
        self.vals[key] = (val, freq)
        return val

    def put(self, key: int, value: int) -> None:
        if self.cap <= 0: return
        if key in self.vals:
            self.get(key)
            self.vals[key] = (value, self.vals[key][1])
        else:
            if self.cap <= len(self.vals):
                k = self.keys[self.minFreq].popitem(last=False)[0]
                self.vals.pop(k)
            self.vals[key] = (value, 1)
            self.minFreq = 1
            self.keys[1][key] = None
            
                


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
