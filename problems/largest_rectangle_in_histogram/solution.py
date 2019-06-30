class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        ans = 0
        stack = [-1]
        for i, h in enumerate(heights):
            while stack[-1] != -1 and heights[stack[-1]] >= h:
                ans = max(ans, heights[stack.pop()] * (i - stack[-1]-1))
            stack.append(i)
        while stack[-1] != -1:
            i = stack.pop()
            ans = max(ans, heights[i] * (len(heights) - 1 - stack[-1]))
        return ans
                                    