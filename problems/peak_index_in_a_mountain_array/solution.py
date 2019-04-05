class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        i = 1
        while i < len(A) and A[i] > A[i-1]:
            i += 1
        return i - 1
        