class Solution:
    def reverseParentheses(self, s: str) -> str:
        if not s: return s
        stack = []
        for c in s:
            # print(stack)
            if c == "(":
                stack.append(c)
            elif c == ")":
                if stack[-1] == "(": stack.pop()
                else:
                    curr = ""
                    while stack[-1] != "(":
                        curr += stack.pop()
                    stack.pop()
                    if not stack or stack[-1] == "(": 
                        stack.append(curr[::-1])
                    else:
                        stack[-1] += curr[::-1]
            else:
                if not stack or stack[-1] == "(": 
                    stack.append(c)
                else:
                    stack[-1] += c
        return stack[0]
        