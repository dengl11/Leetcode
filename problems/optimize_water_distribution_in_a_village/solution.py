class Solution:
    def minCostToSupplyWater(self, n: int, wells: List[int], pipes: List[List[int]]) -> int:
        uf = {i:i for i in range(n + 1)}
        def find(i):
            if uf[i] != i:
                uf[i] = find(uf[i])
            return uf[i]
        pipes = [(c, i, j) for i, j, c in pipes]
        hidden = [(w, 0, i) for i, w in enumerate(wells, 1)]
        res = 0
        for c, i, j in sorted(pipes + hidden):
            ri, rj = find(i), find(j)
            if ri != rj:
                res += c
                uf[ri] = rj
                n -= 1
            if n == 0:
                return res
        