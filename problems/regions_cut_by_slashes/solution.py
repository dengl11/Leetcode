class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        
        mm, nn = len(grid), len(grid[0])
        visited = [[[False]*2 for _ in range(nn)] for _ in range(mm)]
        def explore(m, n, part):
            if visited[m][n][part]: return False
            visited[m][n][part] = True
            if grid[m][n] == ' ':
                visited[m][n][1-part] = True
            if grid[m][n] == '/':
                if part == 0:
                    nexts = [(m - 1, n, 1), (m, n - 1, 4)] # up, left
                else:
                    nexts = [(m + 1, n, 3), (m, n + 1, 2)] # down, right
                
            elif grid[m][n] == '\\':
                if part == 0:
                    nexts = [(m - 1, n, 1), (m, n + 1, 2)] # up, right
                else:
                    nexts = [(m + 1, n, 3), (m, n - 1, 4)] # down, left
            else:
                nexts = [(m - 1, n, 1), (m, n + 1, 2), (m + 1, n, 3), (m, n - 1, 4)]
                
            nexts = [n for n in nexts if n[0]>=0 and n[1]>=0 and n[0] < mm and n[1] < nn]
            for (i, j, direction)  in nexts:
                part = 0
                if direction == 3:
                    part = 0
                elif direction == 1:
                    part = 1
                else:
                    if grid[i][j] == '\\':
                        part = 0 if direction == 4 else 1
                    if grid[i][j] == '/':
                        part = 1 if direction == 4 else 0
                explore(i, j, part)
            return True
        
        ans = 0

        for i in range(mm):
            for j in range(nn):
                for part in [0, 1]:
                    if explore(i, j, part):
                        ans += 1
        return ans
                    



