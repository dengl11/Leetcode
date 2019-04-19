from collections import Counter
class Solution:
    def reorganizeString(self, S: str) -> str:
        c = Counter(S)
        k, ck = c.most_common(1)[0]
        if len(S) - ck < ck-1: return ""
        segments = [k]*ck
        i = 0
        S = sorted(S)
        for c in S:
            if c == k: continue
            # while c == segments[i][-1]:
            #     i = (i + 1) % ck
            segments[i] += c
            i = (i + 1) % ck
            
        return "".join(segments)