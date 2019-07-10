from heapq import heappop, heappush
class Solution(object):
    def assignBikes(self, workers, bikes):
        """
        :type workers: List[List[int]]
        :type bikes: List[List[int]]
        :rtype: int
        """
        def dist(w, b):
            return abs(w[0] - b[0]) + abs(w[1] - b[1])
        
        q = [(0, 0, 0)]
        seen = set()
        while q:
            cost, iw, taken  = heappop(q)
            if (iw, taken) in seen: continue
            seen.add((iw, taken))
            if iw == len(workers): return cost
            for ib, b in enumerate(bikes):
                if taken & (1 << ib): continue
                heappush(q, (cost + dist(workers[iw], b), iw+1, taken | (1 << ib)))