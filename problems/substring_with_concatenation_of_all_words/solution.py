from collections import Counter
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not words or not s: return []
        k = len(words[0])
        WC = Counter(words)
        L = sum(len(w) for w in words)
        ans = []
        for i in range(k):
            curr = Counter()
            left = i
            c = 0
            while i + k <= len(s):
                cw = s[i:i+k]
                if cw not in WC: 
                    curr = Counter()
                    left = i + k
                    c = 0
                else:
                    curr[cw] += 1
                    c += 1
                    while curr[cw] > WC[cw]:
                        curr[s[left:left+k]] -= 1
                        left += k
                        c -=1
                    if c == len(words): 
                        ans.append(left)
                i += k
        return ans
                
                
                
            