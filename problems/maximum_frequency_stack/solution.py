from collections import defaultdict, Counter
class FreqStack:

    def __init__(self):
        self.freq = Counter()
        self.m = defaultdict(list)
        self.most = 0

    def push(self, x: int) -> None:
        self.freq[x] += 1
        self.most = max(self.most, self.freq[x])
        self.m[self.freq[x]].append(x)
        

    def pop(self) -> int:
        val = self.m[self.most].pop()
        self.freq[val] -= 1
        if not self.m[self.most]:
            self.most -= 1
        return val
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(x)
# param_2 = obj.pop()