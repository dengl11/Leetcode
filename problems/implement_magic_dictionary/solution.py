from functools import reduce
from collections import defaultdict
class MagicDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        

    def buildDict(self, words: List[str]) -> None:
        """
        Build a dictionary through a list of words
        """
        self.dic = set()
        for w in words:
            for i in range(len(w)):
                for diff in range(1, 26):
                    c = chr((ord(w[i])-97 + diff)%26 + 97)
                    self.dic.add(w[:i] + c + w[i+1:])
        
        

    def search(self, word: str) -> bool:
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        """
        return word in self.dic


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dict)
# param_2 = obj.search(word)