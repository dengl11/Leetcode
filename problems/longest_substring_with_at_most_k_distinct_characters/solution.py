from collections import Counter
class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        chars = Counter()
        i = 0
        ans = 0
        for j, c in enumerate(s):
            chars[c] += 1
            while len(chars) > k:
                ic = s[i]
                i += 1
                chars[ic] -= 1
                if chars[ic] == 0: del chars[ic]
            ans = max(ans, j - i + 1)
        return ans
            
                
        