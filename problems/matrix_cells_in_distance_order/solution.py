class Solution:
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        visited = [[False]*C for _ in range(R)]
        ans = [[r0, c0]]
        q = [(r0, c0)]
        visited[r0][c0] = True
        while q:
            newq = []
            for (r, c) in q:
                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    cr, cc = r + dx, c + dy
                    if cr < 0 or cr >= R or cc < 0 or cc >= C: continue
                    if visited[cr][cc]: continue
                    visited[cr][cc] = True
                    newq.append([cr, cc])
            ans += newq
            q = newq
        return ans
        