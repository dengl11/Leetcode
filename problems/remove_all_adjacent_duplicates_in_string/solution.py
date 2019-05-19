class Solution:
    def removeDuplicates(self, S: str) -> str:
        s = []
        for c in S:
            if not s or s[-1] != c:
                s.append(c)
            else:
                s.pop()
        return "".join(s) 