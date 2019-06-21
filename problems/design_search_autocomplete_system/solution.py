from collections import defaultdict
from functools import reduce
class AutocompleteSystem:

    def __init__(self, sentences: List[str], times: List[int]):
        T = lambda: defaultdict(T)
        trie = T()
        for s, i in zip(sentences, times):
            reduce(lambda node, c: node[c], s, trie)['$'] = i
        self.trie = trie
        self.node = self.trie
        self.s = ""
    
    def add_sentence(self, s):
        x = reduce(lambda node, c: node[c], s, self.trie).get('$', 0)
        reduce(lambda node, c: node[c], s, self.trie)['$'] = x + 1
        

    def input(self, c: str) -> List[str]:
        if c != '#':
            self.s += c
            
        if self.node and c != '#':
            self.node = self.node[c]
        ans = []
        if c != '#' and self.node:
            stack = [(self.node, self.s)]
            while stack:
                node, s = stack.pop()
                if "$" in node:
                    ans.append((-node['$'], s))
                for k, v in node.items():
                    if k != '$':
                        stack.append((v, s + k))
        ans.sort()
        if c == '#':
            self.add_sentence(self.s)
            self.s = ""
            self.node = self.trie
        return [x[1] for x in ans][:3]
            
            
        
            