from random import randint
class Solution:

    def __init__(self, N: int, blacklist: List[int]):
        self.n = N - len(blacklist)
        B = set(blacklist)
        blacklist = sorted(x for x in blacklist if x < self.n)
        self.m = dict()
        j = 0
        for i in range(self.n, N):
            if i not in B:
                self.m[blacklist[j]] = i
                j += 1

    def pick(self) -> int:
        i = randint(0, self.n-1)
        return i if i not in self.m else self.m[i]
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(N, blacklist)
# param_1 = obj.pick()