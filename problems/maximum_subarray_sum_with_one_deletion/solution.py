class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        premin = 0
        premax = [0]
        curr = 0
        for x in arr:
            curr += x
            premax.append(curr - premin)
            premin = min(premin, curr)
        postmin = 0
        ans = max(premax[1:])
        postmax = [0]
        curr = 0
        for x in arr[::-1]:
            curr += x
            postmax.append(curr - postmin)
            postmin = min(postmin, curr)
        postmax.reverse()
        for i in range(1, len(arr) - 1):
            ans = max(ans, premax[i] + postmax[i + 1])
        return ans
        
        
        
            
        