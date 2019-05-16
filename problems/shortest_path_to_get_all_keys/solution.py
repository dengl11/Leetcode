from collections import deque
class Solution(object):
    def shortestPathAllKeys(self, grid):
        """
        :type grid: List[str]
        :rtype: int
        """
        M, N = len(grid), len(grid[0])
        letters = 0
        for i in range(M):
            for j in range(N):
                if grid[i][j] == "@": start = (i, j)
                elif grid[i][j] in "abcdef": letters += 1
        q = deque([(*start, 0, 0)]) # [(i, j, keys, moves)]
        visited = set([(*start, 0)])
        while q:
            i, j, keys, m = q.popleft()
            if keys == (1<<letters) - 1: return m
            for di, dj in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
                ci, cj = i + di, j + dj
                new_key = keys
                if ci < 0 or ci >= M or cj < 0 or cj >= N: continue
                if grid[ci][cj] == "#": continue
                elif grid[ci][cj] in "ABCDEF": 
                    k = ord(grid[ci][cj]) - ord('A')
                    if keys & (1<<k) == 0: continue
                elif grid[ci][cj] in "abcdef":
                    k = ord(grid[ci][cj]) - ord('a')
                    new_key = keys | (1<<k)
                if (ci, cj, new_key)  in visited: continue
                q.append((ci, cj, new_key, m + 1))
                visited.add((ci, cj, new_key))
        return -1

                    
                    
                