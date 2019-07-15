class Solution:
    def countPrimes(self, n: int) -> int:
        s = set(range(2, n))
        for i in range(2, n):
            if i not in s: continue
            j = i * 2
            while j < n:
                s.discard(j)
                j += i
        return len(s)
        