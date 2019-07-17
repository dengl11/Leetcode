class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        chars = ['$']
        for c in s:
            chars.append(c)
            chars.append('$')
        ans = ""
        for i in range(len(chars)):
            l = 0
            while i - l >= 0 and i + l < len(chars) and chars[i-l] == chars[i+l]:
                l += 1
            curr = "".join(chars[i-l+1:i+l]).replace('$', "")
            if len(curr) > len(ans):
                ans = curr
        return ans
            
                