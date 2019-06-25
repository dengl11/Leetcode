from collections import defaultdict
from functools import reduce
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        if not board or not board[0]: return []
        m, n = len(board), len(board[0])
        T = lambda: defaultdict(T)
        trie = T()
        for w in words:
            reduce(lambda node, c: node[c], w, trie)['$'] = 1
        def check(i, j):
            ans = []
            visited = set([(i, j)])
            def dfs(i, j, s, node):
                if board[i][j] not in node: return
                node = node[board[i][j]]
                s += board[i][j]
                if '$' in node: ans.append(s)
                for ni, nj in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                    if ni >= 0 and ni < m and nj >= 0 and nj < n:
                        if (ni, nj) not in visited:
                            visited.add((ni, nj))
                            dfs(ni, nj, s, node)
                            visited.remove((ni, nj))
            dfs(i, j, "", trie)
            return ans
        ans = []
        for i in range(m):
            for j in range(n):
                ans  += check(i, j)
        return list(set(ans))
                