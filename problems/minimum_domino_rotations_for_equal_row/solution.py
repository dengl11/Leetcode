from collections import Counter

class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        c = Counter(A + B)
        n = len(A)
        candidates = []
        for x, num in c.items():
            if num >= n:
                candidates.append(x)
        
        if not candidates: return -1
        ans = -1
        candidate = candidates[0]
        nA = nB = 0
        for i in range(n):
            if A[i] != candidate and B[i] != candidate:
                return -1
            if A[i] != candidate: nA += 1
            if B[i] != candidate: nB += 1
        return min(nA, nB)

        
        