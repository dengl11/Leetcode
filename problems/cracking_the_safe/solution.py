class Solution:
    def crackSafe(self, n: int, k: int) -> str:
        tgt = k ** n
        start = "0"*n
        visited = set([start])
        chrs = ['0']*n
        def dfs(s):
            if len(visited) == tgt: return True
            pre = s[1:]
            for c in range(k):
                curr = pre + str(c)
                if curr not in visited:
                    visited.add(curr)
                    chrs.append(str(c))
                    if dfs(curr): return True
                    visited.remove(curr)
                    chrs.pop()
            return False
        dfs(start)
        return "".join(chrs)
        
        