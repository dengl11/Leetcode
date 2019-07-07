class Solution(object):
    def corpFlightBookings(self, bookings, n):
        """
        :type bookings: List[List[int]]
        :type n: int
        :rtype: List[int]
        """
        ans = [0] * n
        starts = sorted((x[0], x[-1]) for x in bookings)
        ends = sorted((x[1], x[-1]) for x in bookings)
        i = j = 0
        curr = 0
        for label in range(1, n + 1):
            while i < len(starts) and starts[i][0] <= label:
                curr += starts[i][1]
                i += 1
            while j < len(starts) and ends[j][0] < label:
                curr -= ends[j][1]
                j += 1
            ans[label - 1] = curr
        return ans
                
            