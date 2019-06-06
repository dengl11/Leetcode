from math import log
class Solution:
    def smallestGoodBase(self, n: str) -> str:
        n = int(n)
        for k in range(int(log(n, 2)), 1, -1):
            x = int(n ** (k ** -1))
            if (x ** (k+1)) - 1 == n * (x - 1):
                return str(x)
        return str(n-1)
        