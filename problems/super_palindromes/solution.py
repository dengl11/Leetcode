class Solution(object):
    def superpalindromesInRange(self, L, R):
        """
        :type L: str
        :type R: str
        :rtype: int
        """
        L, R = int(L), int(R)
        ans = 0
        def is_palindrome(s):
            return s == s[::-1]
        for i in range(100000):
            s = str(i)
            ss = s + s[-2::-1]
            sss = int(ss)**2
            if sss > R: break
            if sss < L or not is_palindrome(str(sss)):
                continue
            ans += 1
        for i in range(100000):
            s = str(i)
            ss = s + s[::-1]
            sss = int(ss)**2
            if sss > R:break
            if sss < L or not is_palindrome(str(sss)):
                continue
            ans += 1
        return ans