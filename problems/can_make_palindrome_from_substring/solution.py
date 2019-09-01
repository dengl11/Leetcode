from functools import lru_cache
class Solution:
    def canMakePaliQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
        pre = [[0] * (1 + len(s)) for _ in range(26)]
        for i, c in enumerate(s, 1):
            j = ord(c) - 97
            pre[j][i] += 1
            if i < len(s):
                for j in range(26):
                    pre[j][i + 1] = pre[j][i]
                
        def query(i, j, K):
            k = 0
            for c in range(26):
                if (pre[c][j + 1] - pre[c][i]) % 2:
                    print(c)
                    k += 1
            return K >= k // 2
        return [query(i, j, k) for (i, j, k) in queries]