from collections import Counter
class Solution:
    def reorganizeString(self, S: str) -> str:
        c = Counter(S)
        k, ck = c.most_common(1)[0]
        if len(S) - ck < ck-1: return ""
        segments = [k]*ck
        i = 0
        for ch, cnt in c.items():
            if ch == k: continue
            for _ in range(cnt):
                segments[i] += ch
                i = (i + 1) % ck
            
        return "".join(segments)