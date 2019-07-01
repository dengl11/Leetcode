class Solution:
    def minTotalDistance(self, grid: List[List[int]]) -> int:
        def sumMedian(arr):
            arr.sort()
            ans = 0
            l, r = 0, len(arr) - 1
            while l < r:
                ans += arr[r]- arr[l]
                l += 1
                r -= 1
            return ans
    
        xs, ys = [], []
        for i, r in enumerate(grid):
            for j, x in enumerate(r):
                if x == 1:
                    xs.append(i)
                    ys.append(j)
        return sumMedian(xs) + sumMedian(ys)
        