from collections import defaultdict
class ValidWordAbbr:
    def encode(self, w):
        if len(w) < 3: return w
        return w[0] + str(len(w) - 2) + w[-1]

    def __init__(self, dictionary: List[str]):
        self.data = defaultdict(set)
        for w in set(dictionary):
            self.data[self.encode(w)].add(w)
        

    def isUnique(self, word: str) -> bool:
        e = self.encode(word)
        if e not in self.data: return True
        return self.data[e] == {word}
        


# Your ValidWordAbbr object will be instantiated and called as such:
# obj = ValidWordAbbr(dictionary)
# param_1 = obj.isUnique(word)