from collections import deque
class Solution:
    def minKBitFlips(self, A: List[int], K: int) -> int:
        flipped = deque()
        curr = 0
        ans = 0
        for i, x in enumerate(A):
            if i >= K:
                curr ^= flipped[0] 
            if curr^A[i] != 1: 
                if len(A) - i < K: return -1
                ans += 1
                curr ^= 1
                flipped.append(1)
            else:
                flipped.append(0)
            if len(flipped) > K:
                flipped.popleft()
        return ans
                        
        