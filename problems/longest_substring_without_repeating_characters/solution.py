class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0
        window = set()
        i = 0
        for j, c in enumerate(s):
            while c in window:
                window.remove(s[i])
                i += 1
            window.add(c)
            ans = max(ans, len(window))
        return ans