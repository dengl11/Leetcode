class Solution:
    def minmaxGasDist(self, stations: List[int], K: int) -> float:
        stations.sort()
        
        def count(dist):
            ans = 0
            for i in range(len(stations) - 1):
                D = stations[i+1] - stations[i]
                if D <= dist: continue
                ans += D // dist
            # print(dist, ans)
            return ans
        
        l, r = 0, stations[-1] - stations[0]
        while r - l > 1e-6:
            # print(l, r)
            mid = (l + r) / 2
            c = count(mid)
            # print(c)
            if K >= c:
                r = mid
            else:
                l = mid
        return l
            