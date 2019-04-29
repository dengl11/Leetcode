from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False
        need = Counter(s1)
        for i in range(len(s2)):
            need[s2[i]] -= 1
            if i >= len(s1):
                pre = s2[i-len(s1)]
                need[pre] += 1
                if need[pre] == 0:
                    del need[pre]
            if need[s2[i]] == 0:
                del need[s2[i]]
            if not need: return True
        return False
            
        
        