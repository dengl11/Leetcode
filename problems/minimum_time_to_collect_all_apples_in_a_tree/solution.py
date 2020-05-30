from collections import defaultdict
class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        self.ans = 0
        visited = set()
        nbrs = defaultdict(list)
        for i, j in edges:
            nbrs[i].append(j)
            nbrs[j].append(i)
        def dfs(curr):
            containApple = False
            for nbr in nbrs[curr]:
                if nbr in visited: continue
                visited.add(nbr)
                containApple = dfs(nbr) or containApple
            if curr == 0: return False
            if hasApple[curr] or containApple:
                self.ans += 2
                return True
            return False
        dfs(0)
        return self.ans
                