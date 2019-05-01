class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        n = len(nums)
        visited = [False] * n
        def explore(x):
            if visited[x]: return 0
            visited[x] = True
            return 1 + explore(nums[x])
        return max(explore(i) for i in range(n))
        