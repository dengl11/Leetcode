from heapq import heappush, heappop
class Solution:
    def maximumMinimumPath(self, A: List[List[int]]) -> int:
        m, n = len(A), len(A[0])
        q = [(-A[0][0], 0, 0)]
        done = set((0, 0))
        while q:
            c, i, j = heappop(q)
            if (i, j) == (m-1, n-1):
                return -c
            for ni, nj in [(i+1, j), (i-1, j), (i, j + 1), (i, j-1)]:
                if ni < 0 or ni >= m or nj < 0 or nj >= n: continue
                if (ni, nj) in done: continue
                heappush(q, (-min(-c, A[ni][nj]), ni, nj))
                done.add((ni, nj))
                