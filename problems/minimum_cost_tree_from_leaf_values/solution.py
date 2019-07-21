class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        stack = [float('inf')]
        ans = 0
        for x in arr:
            while stack[-1] <= x:
                mid = stack.pop()
                ans += mid * min(x, stack[-1])
            stack.append(x)
        while len(stack) > 2:
            ans += stack.pop() * stack[-1]
        return ans