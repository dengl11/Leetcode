from collections import deque
class Solution:
    def shortestSuperstring(self, A: List[str]) -> str:
        def dist(si, sj):
            for i in range(1, len(si)):
                if sj.startswith(si[i:]): return len(si) - i
            return 0
        n = len(A)
        G = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if i == j: continue
                G[i][j] = dist(A[i], A[j])
        D = [[0]*n for i in range(1<<n)]
        q = deque()
        for i in range(n):
            q.append((i, 1 << i, [i], 0))
        P, L = None, -1
        while q:
            curr, mask, path, save = q.popleft()
            if save < D[mask][curr]: continue
            if len(path) == n:
                if save > L:
                    L = save
                    P = path
            else:
                for j in range(n):
                    if mask & (1<<j): 
                        continue
                    nextMask = mask | (1<<j)
                    if D[mask][curr] + G[curr][j] >= D[nextMask][j]:
                        D[nextMask][j] = D[mask][curr] + G[curr][j]
                        q.append((j, nextMask, path+[j], D[nextMask][j]))
        # construct the string
        ans = ""
        pre = -1
        P = P[::-1]
        while P:
            i = P.pop()
            if pre < 0: 
                ans += A[i]
            else:
                ans += A[i][G[pre][i]:]
            pre = i
        return ans
                
            
        
                    
        