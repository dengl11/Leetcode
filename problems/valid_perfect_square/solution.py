class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left, right = 1, num
        while left <= right:
            mid = (left + right + 1) // 2
            curr =  mid ** 2
            if curr == num: return True
            if curr < num:
                left = mid + 1
            else:
                right = mid - 1
        return False
        