class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        def valid(x):
            curr = x
            while curr:
                if curr % 10 == 0: return False
                if x % (curr % 10) != 0: return False
                curr //= 10
            return True
        return [x for x in range(left, right + 1) if valid(x)]