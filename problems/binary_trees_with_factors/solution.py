from collections import Counter
class Solution:
    def numFactoredBinaryTrees(self, A: List[int]) -> int:
        c = Counter(A)
        A.sort()
        for i in range(1, len(A)):
            x = A[i]
            for j in range(i):
                y = A[j]
                if x // y in c and x//y * y == x:
                    c[x] +=  c[x//y] * c[y]
        return sum(c.values()) % (10 ** 9 + 7)              