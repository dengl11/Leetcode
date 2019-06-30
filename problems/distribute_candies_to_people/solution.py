class Solution:
    def distributeCandies(self, candies: int, n: int) -> List[int]:
        round = 0
        full = n * (n+1)//2
        while candies > full:
            candies -= full
            round += 1
            full = round * n * n + n * (n+1)//2
        ans = [(i+1) * round + round * (round - 1) // 2 * n for i in range(n)]
        # print(ans, candies)
        j = 0
        while candies > 0:
            # print(ans, candies)
            alloc = j + 1 + round * n
            ans[j] += min(candies, alloc)
            candies -= alloc
            j += 1
        return ans
            
        