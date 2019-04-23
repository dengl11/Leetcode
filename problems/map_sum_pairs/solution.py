from collections import defaultdict
from functools import reduce
class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        T = lambda:defaultdict(T)
        self.trie = T()
        

    def insert(self, key: str, val: int) -> None:
        reduce(dict.__getitem__, key, self.trie)['#'] = val
        
        

    def sum(self, prefix: str) -> int:
        node = reduce(dict.__getitem__, prefix, self.trie)
        ans = 0
        stack = [node]
        while stack:
            node = stack.pop()
            val = node.pop('#', 0)
            ans += val
            stack += node.values()
            node['#'] = val
        return ans
        


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)