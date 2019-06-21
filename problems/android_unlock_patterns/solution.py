class Solution:
    def numberOfPatterns(self, m: int, n: int) -> int:
        self.c = 0
        between = dict()
        between[(1, 3)] = 2
        between[(3, 1)] = 2
        between[(7, 1)] = 4
        between[(1, 7)] = 4
        between[(1, 9)] = 5
        between[(9, 1)] = 5
        between[(2, 8)] = 5
        between[(8, 2)] = 5
        between[(3, 7)] = 5
        between[(7, 3)] = 5
        between[(3, 9)] = 6
        between[(9, 3)] = 6
        between[(4, 6)] = 5
        between[(6, 4)] = 5
        between[(7, 9)] = 8
        between[(9, 7)] = 8
        
        def dfs(i, used):
            used.add(i)
            if m <= len(used) <= n:
                self.c += 1
            if len(used) < n:
                for ni in range(1, 10):
                    if ni in used or ni == i: continue
                    if (i, ni) in between and between[(i, ni)] not in used: continue
                    used.add(ni)
                    dfs(ni, used)
                    used.remove(ni)
        for i in range(1, 10):
            dfs(i, set())
        return self.c