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
        q = []
        W = []
        for ib, b in enumerate(bikes):
            curr = sorted([(dist(w, b), iw, ib) for iw, w in enumerate(workers)], reverse=True)
            heappush(q, curr.pop())
            W.append(curr)
            
        ans = dict()
        while len(ans) < len(workers):
            d, iw, ib = heappop(q)
            if iw not in ans:
                ans[iw]  = ib
            else:
                heappush(q, W[ib].pop())
        return [ans[i] for i in range(len(workers))]
                
                
            
            