class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        colors = [0] * len(nums)
        def dfs(i, direction = 0):
            if colors[i] < 0: return False
            colors[i] = 1 # in-exploration
            ni = i + nums[i] + len(nums)
            while ni < 0:
                ni += len(nums)
            ni = ni % len(nums)
            next_dir = 1 if nums[ni] > 0 else -1
            ans = True
            if direction!= 0 and next_dir != direction:
                ans = False
            elif i == ni:
                ans = False
            elif colors[ni] == 1:
                ans = True
            else:
                ans = dfs(ni, next_dir)
            if not ans: colors[i] = -1
            return ans
        
        return any(dfs(i) for i in range(len(nums)))