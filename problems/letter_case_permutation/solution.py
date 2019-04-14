class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        ans = []
        stack = [(S, 0)]
        while stack:
            s, i = stack.pop()
            if i == len(s): ans.append(s)
            else:
                if s[i].isalpha():
                    stack.append((s[:i] + (s[i].upper() if s[i].islower() else s[i].lower()) + s[i+1:], i+1))
                stack.append((s, i + 1))
        return ans
                    
        