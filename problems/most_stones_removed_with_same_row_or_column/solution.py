from collections import defaultdict
class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        stones = [tuple(x) for x in stones]
        row, col = defaultdict(list), defaultdict(list)
        for i, j in stones:
            row[i].append((i, j))
            col[j].append((i, j))
        visited = set()
        def dfs(i, j):
            visited.add((i, j))
            ans = 1
            for ni, nj in row[i] + col[j]:
                if (ni, nj) in visited: continue
                ans += dfs(ni, nj)
            return ans
        ans = 0
        for i, j in stones:
            if (i, j) in visited: continue
            ans += dfs(i, j) - 1
        return ans