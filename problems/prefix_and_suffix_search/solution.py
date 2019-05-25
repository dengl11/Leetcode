from collections import defaultdict
from functools import reduce
class WordFilter:

    def __init__(self, words: List[str]):
        T = lambda : defaultdict(T)
        self.trie = T()
        self.words = words
        for i, w in enumerate(words):
            reduce(lambda t, c:t[c], w, self.trie)['$'] = i
    
    def collect(self, prefix):
        node = self.trie
        for c in prefix:
            node = node[c]
        q = [node]
        for n in q: # BFS
            if '$' in n: yield n['$']
            for k, v in n.items():
                if k != '$':
                    q.append(v)
            
        

    def f(self, prefix: str, suffix: str) -> int:
        ans = -1
        for i in self.collect(prefix):
            if self.words[i].endswith(suffix):
                if i > ans:
                    ans = i
        return ans
        


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix,suffix)