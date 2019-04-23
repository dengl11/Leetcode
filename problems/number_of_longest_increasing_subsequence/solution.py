class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        if not nums: return 0
        n = len(nums)
        L = 1
        Ls = [1] * n
        options = [1] * n
        for i in range(1, len(nums)):
            curr = 1
            for j in range(i):
                if nums[j] < nums[i]:
                    curr = max(curr, 1 + Ls[j])
            Ls[i] = curr
            if curr == 1:
                continue
            options[i] = 0
            for j in range(i):
                if Ls[j] == curr-1 and nums[j] < nums[i]:
                    options[i] += options[j]
            L = max(L, curr)
        # print(options)
        # print(Ls)
        return sum(options[i] for i in range(n) if Ls[i] == L)
        