class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        dst = tuple(destination)
        m, n = len(maze), len(maze[0])
        def stop(i, j, di, dj):
            while i + di >= 0 and i + di < m and j + dj >=0 and j + dj < n and maze[i+di][j+dj] == 0:
                i += di
                j += dj
            return i, j
        
        visited = set([tuple(start)])
        def query(i, j):
            if (i, j) == dst: return True
            for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                ni, nj = stop(i,j, di, dj)
                if (ni, nj) in visited: continue
                visited.add((ni, nj))
                if query(ni, nj): return True
            return False
        
        return query(*start)
            
        