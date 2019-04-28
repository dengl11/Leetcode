class Solution:
    def colorBorder(self, grid: List[List[int]], r0: int, c0: int, color: int) -> List[List[int]]:
        borders = []
        m, n = len(grid), len(grid[0])
        def ner(x, y):
            for dx, dy in [(0,1), (0, -1), (1, 0), (-1, 0)]:
                cx, cy = dx + x, dy + y
                if cx < 0 or cx >= m or cy < 0 or cy >= n: continue
                yield (cx, cy)
            
        def is_border(x, y):
            if x == 0 or x == m-1 or y == 0 or y == n-1: return True
            curr = grid[x][y]
            for cx, cy in ner(x, y):
                if grid[cx][cy] != curr: return True
            return False
        
        stack = [(r0, c0)]
        visited = set([(r0, c0)])
        while stack:
            r, c = stack.pop()
            if is_border(r, c): borders.append((r, c))
            for cx, cy in ner(r, c):
                if (cx, cy) in visited or grid[cx][cy] != grid[r0][c0]: continue
                stack.append((cx, cy))
                visited.add((cx, cy))
        for x, y in borders:
            grid[x][y] = color
        return grid