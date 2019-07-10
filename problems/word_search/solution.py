from collections import defaultdict
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not board or not board[0]: return False
        if not word: return True
        
        def find(i, j):
            visited = set([(i, j)])
            def dfs(i, j, k):
                if k >= len(word): return True
                for ni, nj in [(i + 1, j), (i-1, j), (i, j+1), (i, j-1)]:
                    if ni < 0 or ni >= m or nj < 0 or nj >= n: continue
                    if board[ni][nj] != word[k] or (ni, nj) in visited: continue
                    visited.add((ni, nj))
                    if dfs(ni, nj, k + 1): return True
                    visited.remove((ni, nj))
                return False
            return dfs(i, j, 1)
        
        s = word[0]
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                if s == board[i][j] and find(i, j):
                    return True
        return False
                    
        
        
        