class Solution:
    def isIdealPermutation(self, A: List[int]) -> bool:
        currMax = -1
        pre = -1
        for i, x in enumerate(A):
            if currMax > x: return False
            currMax = max(currMax, pre)
            pre = x
        return True
            