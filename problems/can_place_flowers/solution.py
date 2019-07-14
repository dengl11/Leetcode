class Solution(object):
    def canPlaceFlowers(self, f, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        for i in range(len(f)):
            if not n: return True
            if f[i]:continue
            if (i > 0 and f[i-1]) or (i < len(f) - 1 and f[i+1]): continue
            f[i] = 1
            n -= 1
        return n == 0
                
                