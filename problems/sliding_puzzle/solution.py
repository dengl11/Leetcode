class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        s = tuple(board[0] + board[1])
        dirs = [(1, 3), (0, 2, 4), (1, 5), (0, 4), (1, 3, 5), (2, 4)]
        q = [s]
        ans = 0
        visited = set([s])
        def swap(x, i, j):
            nx = list(x)
            nx[i], nx[j] = nx[j], nx[i]
            return tuple(nx)
            
        while q:
            newq = []
            for x in q:
                if x == (1,2,3,4,5,0): return ans
                i = x.index(0)
                for d in dirs[i]:
                    nx = swap(x, i, d)
                    if nx not in visited:
                        visited.add(nx)
                        newq.append(nx)
            ans += 1
            q = newq
        return -1                