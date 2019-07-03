from collections import defaultdict
from functools import reduce

class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        T = lambda: defaultdict(T)
        self.trie = T()
        

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        reduce(lambda node, c: node[c], word, self.trie)['$'] = 1
    
        

    def search(self, word: str, node = None) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        node = node or self.trie
        for i, c in enumerate(word):
            if c == '.':
                return any(self.search(word[i+1:], node[k]) for k in node if k != '$')
            if c not in node: return False
            node = node[c]
        return '$' in node
            
            


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)