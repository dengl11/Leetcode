class RLEIterator:

    def __init__(self, A: List[int]):
        pairs = []
        for i in range(0, len(A), 2):
            m, n = A[i], A[i+1]
            if m > 0:
                pairs.append([m, n])
        self.pairs = pairs[::-1]

    def next(self, n: int) -> int:
        if not self.pairs: return -1
        if n > self.pairs[-1][0]:
            n -= self.pairs.pop()[0]
            return self.next(n)
        self.pairs[-1][0] -= n
        ans = self.pairs[-1][1]
        if self.pairs[-1][0] == 0:
            self.pairs.pop()
        return ans
        


# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator(A)
# param_1 = obj.next(n)