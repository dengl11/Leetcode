class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        def encode(s):
            return "".join(x for x in s if x!="X")
        if encode(start) != encode(end): return False
        i = j = 0
        while i < len(start) and j < len(end):
            if start[i] == "X": 
                i += 1
                continue
            if end[j] == "X": 
                j += 1
                continue
            if start[i] == "L" and i < j: return False
            if start[i] == "R" and i > j: return False
            i += 1
            j += 1
        return True