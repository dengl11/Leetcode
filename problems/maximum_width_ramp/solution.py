class Solution:
    def maxWidthRamp(self, A: List[int]) -> int:
        pos = sorted((x, i) for (i, x) in enumerate(A))
        pos = [m[1] for m in pos]
        pre = pos[0]
        ans = 0
        for x in pos[1:]:
            ans = max(ans, x - pre)
            pre = min(pre, x)
        return ans
            
            
        