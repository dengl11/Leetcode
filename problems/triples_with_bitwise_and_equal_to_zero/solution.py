from collections import Counter
class Solution:
    def countTriplets(self, A: List[int]) -> int:
        c = Counter()
        ans = 0
        for i in range(len(A)):
            for j in range(len(A)):
                c[A[i] & A[j]] += 1
        for i in range(len(A)):
            for k, v in c.items():
                if A[i] & k == 0:
                    ans += v
        return ans