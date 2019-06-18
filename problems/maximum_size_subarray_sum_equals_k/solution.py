class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        n = len(nums)
        acc = [0] * (n+1)
        pos = {0:-1} # {sum: first position}
        ans = 0
        for i, x in enumerate(nums):
            acc[i+1] = acc[i] + x
            pre = acc[i+1] - k
            if pre in pos:
                ans = max(ans, i-pos[pre])
            if acc[i+1] not in pos:
                pos[acc[i+1]] = i
        return ans
        