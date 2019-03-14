class Solution:
    def largestSumAfterKNegations(self, A: List[int], K: int) -> int:
        negs = []
        pos = []
        zeros = 0
        for x in A:
            if x < 0:
                negs.append(x)
            elif x == 0:
                zeros += 1
            else:
                pos.append(x)
        
        if K <= len(negs):
            negs.sort()
            return sum(pos) - sum(negs[:K]) + sum(negs[K:])
        if zeros > 0 or (K - len(negs)) % 2 == 0:
            return sum(pos) - sum(negs)
        return sum(pos) - sum(negs) - 2 * min(abs(x) for x in A)
        
            
        