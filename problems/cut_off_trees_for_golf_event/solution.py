from collections import deque
class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        m, n = len(forest), len(forest[0])
        visited = set([(0, 0)])
        stack = [(0, 0)]
        trees = sorted([(forest[i][j], i, j) for i in range(m) for j in range(n) if forest[i][j] > 1])
        def nbr(i, j):
            for ni, nj in [(i, j + 1), (i, j - 1), (i+1, j), (i-1, j)]:
                if ni < 0 or ni >= m or nj < 0 or nj >= n: continue
                if forest[ni][nj] == 0: continue
                yield (ni, nj)
                
        while stack:
            i, j = stack.pop()
            for ni, nj in nbr(i, j):
                if (ni, nj) in visited: continue
                visited.add((ni, nj))
                stack.append((ni, nj))
        if sum(forest[i][j] > 1 for (i, j) in visited) != len(trees): return -1
        
        ans = 0
        def dist(i, j, ti, tj):
            return abs(i-ti) + abs(j-tj)
        ci = cj = 0
        for _, I, J in trees: 
            q = [(ci, cj)]
            nexts = []
            curr = dist(ci, cj, I, J)
            visited = set()
            while q or nexts:
                if not q:
                    q = nexts
                    nexts = []
                    curr += 2
                i, j = q.pop()
                if (i, j) == (I, J):
                    break
                if (i, j) in visited: continue
                visited.add((i, j))
                for ni, nj in nbr(i, j):
                    if (ni, nj) in visited: continue
                    closer = dist(ni, nj, I, J) < dist(i, j, I, J)
                    if closer: q.append((ni, nj))
                    else: nexts.append((ni, nj))
            ci = I
            cj = J
            ans += curr
        return ans
            
                
            
            
                
            
            
            
        