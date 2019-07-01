class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        ans = 0
        for _ in range(2):
            rights = [-1] * n
            stack = []
            for i, h in enumerate(height):
                while stack and height[stack[-1]] <= h:
                    rights[stack.pop()] = i
                stack.append(i)
            i = 0
            while i < n:
                if rights[i] < 0:
                    i += 1
                else:
                    # if i > 0 and height[]
                    for k in range(i+1, rights[i]):
                        ans += height[i] - height[k]
                        height[k] = height[i]
                    i = rights[i]
            height.reverse()
        return ans


