from heapq import heappop, heappush
class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        n = len(workers)
        def dist(w, b):
            return abs(w[0]-b[0]) + abs(w[1]-b[1])
        todos = [None for _ in range(len(bikes))]
        for j, b in enumerate(bikes):
            todos[j] = sorted((dist(b, workers[i]), i, j) for i in range(n))
        starts = [0] * len(bikes)
        q = []
        for i in range(len(bikes)):
            heappush(q, todos[i][0])
        ans = [-1] * n
        while n:
            dist, iw, ib = heappop(q)
            if ans[iw] >= 0:
                if starts[ib] + 1 < len(workers):
                    starts[ib] += 1
                    heappush(q, todos[ib][starts[ib]])
            else:
                ans[iw] = ib
                n -= 1
        return ans