class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        ans = [0] * len(T)
        stack = []
        for j, x in enumerate(T):
            while stack and T[stack[-1]] < x:
                i = stack.pop()
                ans[i] = j-i
            stack.append(j)
        return ans