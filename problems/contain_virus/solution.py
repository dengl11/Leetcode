class Solution(object):
    def containVirus(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        def nbr(i, j):
            return [(i+di, j+dj) for (di, dj) in [(0, 1), (0, -1), (1, 0), (-1, 0)] if i+di>=0 and i + di < m and j + dj >= 0 and j+dj < n]
            
            
        def find_region(i, j, visited):
            if grid[i][j] <= 0 or (i, j) in visited: return False
            visited.add((i, j))
            stack = [(i, j)]
            while stack:
                i, j = stack.pop()
                for ni, nj in nbr(i, j):
                    if (ni, nj) not in visited and grid[ni][nj] > 0:
                        visited.add((ni, nj))
                        stack.append((ni, nj))
            return True
        
        def process():
            regions = dict()
            r = 1
            visited = set()
            for i in range(m):
                for j in range(n):
                    if find_region(i, j, visited):
                        regions[r] = (i, j)
                        r += 1
            return regions

        def infects(i, j):
            # return (infect_sources, infected_cells)
            infect_sources = 0
            infected_cells = []
            visited = set([(i, j)])
            stack = [(i, j)]
            while stack:
                i, j = stack.pop()
                for ni, nj in nbr(i, j):
                    if grid[ni][nj] == 0: 
                        infect_sources += 1
                    if (ni, nj) in visited or grid[ni][nj] < 0: continue
                    visited.add((ni, nj))
                    if grid[ni][nj] == 0: 
                        infected_cells.append((ni, nj))
                    elif grid[ni][nj] > 0:
                        stack.append((ni, nj))
            return (infect_sources, infected_cells)
         
        def cure(i, j):
            stack = [(i, j)]
            while stack:
                i, j = stack.pop()
                grid[i][j] = -1
                for ni, nj in nbr(i, j):
                    if grid[ni][nj] != 1: continue
                    stack.append((ni, nj))
        
        ans = 0
        while 1:
            regions = process()
            worst_region = walls = -1
            infected = None
            affected = dict()
            for r, (i, j) in regions.items():
                infect_sources, infected_cells = infects(i, j)
                affected[r] = infected_cells
                if infected is None or len(infected_cells) > len(infected):
                    # print(r, infected_cells)
                    infected = infected_cells
                    worst_region = r
                    walls = infect_sources
            if infected is None: return ans
            ans += walls
            i, j = regions[worst_region]
            cure(i, j)
            affected.pop(worst_region)
            for r in affected.values():
                for i, j in r:
                    grid[i][j] = 1
            
                    
            
            