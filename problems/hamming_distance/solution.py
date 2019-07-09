class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        ans = 0
        while x or y:
            ans += (x & 1) != (y & 1)
            x >>= 1
            y >>= 1
        return ans
            
            
        