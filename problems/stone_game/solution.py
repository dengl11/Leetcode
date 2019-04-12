class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        cache = {} # {(i, j): most(piles[i: j + 1])}
        def query(i, j):
            if i == j - 1:
                return max(piles[i: i + 2])
            if (i, j) in cache: return cache[(i, j)]
            ans = max(piles[i] + min(query(i + 2, j), query(i + 1, j-1)), piles[j] + min(query(i, j-2), query(i+1, j-1)))
            cache[(i, j)] = ans
            return ans
        return query(0, len(piles) - 1) > sum(piles) // 2