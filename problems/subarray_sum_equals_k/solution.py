from collections import Counter
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        pre = Counter({0:1})
        ans = 0
        curr = 0
        for x in nums:
            curr += x
            ans += pre[curr - k]
            pre[curr] += 1
        return ans
            