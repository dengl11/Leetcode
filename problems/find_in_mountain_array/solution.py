# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mtn: 'MountainArray') -> int:
        n = mtn.length()
        # find the index
        left, right = 0, n-1
        while left < right:
            m = (left + right) // 2
            if mtn.get(m) < mtn.get(m+1):
                left = peak = m + 1
            else:
                right = m
        # search in the first half
        left, right = 0, peak
        while left <= right:
            m = (left + right) // 2
            curr = mtn.get(m)
            if curr < target:
                left = m + 1
            elif curr == target: 
                return m
            else:
                right = m - 1
        # search in the second half
        left, right = peak, n-1
        while left <= right:
            m = (left + right) // 2
            curr = mtn.get(m)
            if curr < target:
                right = m - 1
            elif curr == target: 
                return m
            else:
                left = m + 1
        return -1
        