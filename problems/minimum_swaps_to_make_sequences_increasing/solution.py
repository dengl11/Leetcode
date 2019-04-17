class Solution:
    def minSwap(self, A: List[int], B: List[int]) -> int:
        keep = 0
        swap = 1
        inf = float('inf')
        for i in range(1, len(A)):
            nextswap = nextkeep = inf
            if A[i] > A[i-1] and B[i] > B[i-1]:
                nextkeep = keep
                nextswap = swap + 1
            if A[i] > B[i-1] and B[i] > A[i-1]:
                nextswap = min(nextswap, keep + 1)
                nextkeep = min(nextkeep, swap)
            keep, swap = nextkeep, nextswap
        return min(keep, swap)
                
                
                    
                