class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        parts = []
        stack = []
        left = 0
        for c in S:
            if c == '(':
                stack.append(c)
                left += 1
            else:
                left -= 1
                if left == 0:
                    parts.append("".join(stack[1:]))
                    stack = []
                else:
                    stack.append(c)
        return "".join(parts)