from collections import deque
class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        def isvalid(s):
            c = 0
            for ch in s:
                if ch == ")": c -= 1
                elif ch == "(": c += 1
                if c < 0: return False
            return c == 0

        ans = []
        visited = set([s])
        q = deque([s])
        found = False
        while q:
            s = q.popleft()
            if isvalid(s):
                ans.append(s)
                found = True
                continue
            if found: continue
            for i in range(len(s)):
                if s[i] not in "()": continue
                ns = s[:i] + s[i+1:]
                if ns in visited: continue
                visited.add(ns)
                q.append(ns)
        return ans
        