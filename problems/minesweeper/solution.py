from itertools import product
class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        i, j = click
        if board[i][j] == 'M':
            board[i][j] = 'X'
            return board
        def ner(i, j):
            for di, dj in product((-1, 0, 1), (-1, 0, 1)):
                if di == 0 and dj == 0: continue
                ci, cj = i + di, j + dj
                if ci < 0 or ci >= len(board) or cj < 0 or cj >= len(board[0]): continue
                yield (ci, cj)
        def mines(i, j):
            ans = 0
            for ni, nj in ner(i, j):
                if board[ni][nj] == "M":
                    ans += 1
            return ans
            
        visited = {(i, j)}
        stack = [(i, j)]
        n = mines(i, j)
        board[i][j] = str(n) if n else 'B'
        if n: return board
        while stack:
            i, j = stack.pop()
            for ni, nj in ner(i, j):
                if (ni, nj) not in visited and board[ni][nj] == "E":
                    visited.add((ni, nj))
                    n = mines(ni, nj)
                    board[ni][nj] = str(n) if n else 'B'
                    if n == 0:
                        stack.append((ni, nj))
                    
        return board
                        
                    
        