class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        def encode(s):
            stack = []
            for c in s:
                if c != '#':
                    stack.append(c)
                elif stack:
                    stack.pop()
            return stack
        return encode(S) == encode(T)
        
        