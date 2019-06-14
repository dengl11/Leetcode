class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = []
        for i, c in enumerate(s):
            if not stack or c == "(":
                stack.append(i)
            elif s[stack[-1]] == ")":
                stack.append(i)
            else:
                stack.pop()
        stack = [-1] + stack + [len(s)]
        return max(stack[i]-stack[i-1]-1 for i in range(1, len(stack)))
