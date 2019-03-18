class Solution:
    def bitwiseComplement(self, N: int) -> int:
        if N == 0: return 1
        firstIdx = -1
        n = N
        while n:
            firstIdx += 1
            n >>= 1
        ans = 0
        for i in range(firstIdx):
            if (N & (1 << i)) == 0:
                ans += 1 << i
        return ans
            
        