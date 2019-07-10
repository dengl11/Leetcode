class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        s = "1"
        for _ in range(n-1):
            ns = ""
            i = 0
            while i < len(s):
                j = i
                i += 1
                while i < len(s) and s[i] == s[i-1]:
                    i += 1
                ns += str(i-j) + s[j]
            s = ns
        return s
        