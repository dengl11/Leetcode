from collections import defaultdict, Counter
from functools import lru_cache
class Solution:
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        @lru_cache(None)
        def hash(w):
            ans = 0
            for c in w:
                ans |= 1 << (ord(c) - 97)
            return ans
        words = Counter([hash(w) for w in words])
        ans = []
        for p in puzzles:
            curr = mask = hash(p)
            t = 0
            first = ord(p[0]) - 97
            while curr:
                if curr & (1 << first):
                    t += words[curr]
                curr = (curr - 1) & mask
            ans.append(t)
        return ans
#         words = sorted([hash(w) for w in words])
#         pre = [[0] * (len(words) + 1) for _ in range(26)]
#         for ic in range(26):
#             for j in range(1, len(words) + 1):
#                 pre[ic][j] = pre[ic][j-1] + int((words[j-1] & (1 << ic)) > 0)
        
#         iw = len(words) - 1
#         ans = [0] * len(puzzles)
#         for p, i in sorted([(p, i) for (i, p) in enumerate(puzzles)], reverse = True):
#             h = hash(p)
#             while iw >= 0 and words[iw] > h:
#                 iw -= 1
#             if iw < 0: 
#                 break
            
#             ans[i] = pre[ord(p[0]) - 97][iw + 1]
#         return ans
            