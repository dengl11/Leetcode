class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        def groups(k):
            # return True if k can be the maximum group sum
            g = 1
            curr = 0
            for x in nums:
                if curr + x > k:
                    curr = x
                    g += 1
                else:
                    curr += x
            return g
        low = max(nums)
        high = sum(nums)
        while low < high:
            mid = (low + high) // 2
            g = groups(mid)
            if g <= m:
                high = mid
            elif g > m:
                low = mid + 1
        assert low == high
        return low
            
                
                    

