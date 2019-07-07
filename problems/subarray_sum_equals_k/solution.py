from collections import Counter
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        pre = [0] * (n + 1)
        for i, x in enumerate(nums):
            pre[i+1] = pre[i] + x
        ans = 0
        c = Counter()
        for x in pre:
            ans += c[x - k]
            c[x] += 1
        return ans
        