from collections import defaultdict, deque
class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:from collections import deque, defaultdict
class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        N = n * n
        visited = [False] * (N + 1)
        skips = [-1] * (N + 1)
        for i in range(n):
            for j in range(n):
                if board[i][j] < 0: continue
                if (n-i-1) % 2 == 0:
                    no = n * (n-i-1) + j + 1
                else:
                    no = n * (n-i) - j
                skips[no] = board[i][j]
        q = deque([(1, 0)])
        # print(sources)
        visited[1] = True
        while q:
            # print(q)
            pos, cost = q.popleft()
            if pos == N: return cost
            cost += 1
            for n in range(pos + 1, min(pos + 6, N) + 1):
                if skips[n] >= 0:
                    n = skips[n]
                if visited[n] : continue
                visited[n] = True
                q.append((n, cost))
        return -1
                
            
        
        
        