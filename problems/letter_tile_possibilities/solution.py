from collections import Counter
class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        c = Counter(tiles)
        self.ans = 0
        def dfs(counter):
            if not counter: return
            self.ans += len(counter)
            for k in list(counter.keys()):
                counter[k] -= 1
                if not counter[k]: del counter[k]
                dfs(counter)
                counter[k] += 1
        dfs(c)
        return self.ans
                