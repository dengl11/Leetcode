class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        result = 1
        k -= 1
        while k > 0:
            interval = [result, result + 1]
            count = 0
            while interval[0] <= n:
                count += min(n+1, interval[1]) - interval[0]
                interval = [x*10 for x in interval]
            if k >= count:
                k -= count
                result += 1
            else:
                k -= 1
                result *= 10
        return result
        