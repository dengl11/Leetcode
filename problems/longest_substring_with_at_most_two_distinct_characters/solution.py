from collections import Counter
class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        c = Counter()
        i = 0
        ans = 0
        for j, ch in enumerate(s):
            c[ch] += 1
            while len(c) > 2:
                c[s[i]] -= 1
                if c[s[i]] == 0: del c[s[i]]
                i += 1
            ans = max(ans, j-i + 1)
        return ans
                
        