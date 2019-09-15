class Solution:
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        def helper(arr):
            premin = 0
            curr = 0
            ma = 0
            for x in arr:
                curr += x
                ma = max(ma, curr - premin)
                premin = min(premin, curr)
            return ma
        
        if k == 1: return helper(arr)
        arr2 = arr + arr
        ma = helper(arr2)
        s = sum(arr)
        if s < 0: 
            ans = ma
        else:
            ans = ma + s * (max(0, k - 2))
        return ans % (10** 9 + 7)
            
        