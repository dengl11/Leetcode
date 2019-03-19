class Solution:
    def isValid(self, S: str) -> bool:
        stack = []
        for ch in S:
            stack.append(ch)
            if stack[-3:] == ['a', 'b', 'c']:
                stack.pop()
                stack.pop()
                stack.pop()
        return not stack