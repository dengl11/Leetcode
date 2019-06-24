# The knows API is already defined for you.
# @param a, person a
# @param b, person b
# @return a boolean, whether a knows b
# def knows(a, b):

class Solution(object):
    def findCelebrity(self, n):
        """
        :type n: int
        :rtype: int
        """
        candidates = set(range(n))
        while candidates:
            c = candidates.pop()
            ok = True
            for x in range(n):
                if x == c: continue
                if knows(x, c):
                    candidates.discard(x)
                else:
                    ok = False
                    break
            if ok and not any(knows(c, x) for x in range(n) if x != c): 
                return c
        return -1