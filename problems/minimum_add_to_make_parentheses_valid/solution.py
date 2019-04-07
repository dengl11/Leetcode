class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        stack = []
        for c in S:
            if stack and (stack[-1] == '(' and c == ')'):
                stack.pop()
            else:
                stack.append(c)
        return len(stack)
            