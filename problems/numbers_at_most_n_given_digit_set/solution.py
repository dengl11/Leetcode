class Solution(object):
    def atMostNGivenDigitSet(self, D, N):
        """
        :type D: List[str]
        :type N: int
        :rtype: int
        """
        N = str(N)
        ans = 0
        n = len(N)
        for i in range(1, n):
            ans += len(D) ** i
        for i in range(n):
            if all(x > N[i] for x in D): break
            candidates = [x for x in D if x < N[i]]
            ans += len(candidates) * len(D) ** (n-1-i)
            if N[i] in D:
                if i == n-1:  ans += 1
            else: break
        return ans
        