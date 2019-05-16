from heapq import heappush, heappop
class Solution(object):
    def minRefuelStops(self, target, startFuel, stations):
        """
        :type target: int
        :type startFuel: int
        :type stations: List[List[int]]
        :rtype: int
        """
        q = []     
        curr = startFuel
        ans = 0
        i = -1
        while curr < target:
            for j in range(i+1, len(stations)):
                if stations[j][0] > curr: break
                heappush(q, -stations[j][1])
                i += 1
            if not q: return -1
            curr += -heappop(q)
            ans += 1
        return ans
                          
                
            