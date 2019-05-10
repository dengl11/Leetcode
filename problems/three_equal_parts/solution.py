class Solution:
    def threeEqualParts(self, A: List[int]) -> List[int]:
        n = len(A)
        ones = []
        for i in range(n):
            if A[i]: ones.append(i)
        none = len(ones)
        if none == 0: return [0, n-1]
        if none % 3: return [-1, -1]
        g = none // 3
        i, j = ones[g-1], ones[2*g -1]
        pre_zero = n-1 - ones[-1]
        if ones[g] - ones[g-1]-1 < pre_zero or ones[2*g]-ones[2*g-1]-1 < pre_zero: 
            return [-1, -1]
        
        i += pre_zero
        j += pre_zero
        k = n-1
        ans = [i, j+1]
        for _ in range(g):
            if not (A[k]==A[j]==A[i]): return [-1, -1]
            k -=1
            j -= 1
            i -= 1
        return ans
        