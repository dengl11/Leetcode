from collections import defaultdict
from string import ascii_lowercase
class Solution:
    def canConvert(self, str1: str, str2: str) -> bool:
        if str1 == str2: return True
        m = dict()
        for c1, c2 in zip(str1, str2):
            if m.get(c1, c2) != c2: 
                return False
            m[c1] = c2
        return len(set(m.values())) < 26
