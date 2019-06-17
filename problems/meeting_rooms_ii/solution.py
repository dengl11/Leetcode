class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        starts = sorted(x[0] for x in intervals)
        ends = sorted(x[1] for x in intervals)
        ans = 0
        curr = j = 0
        for s in starts:
            curr += 1
            while j < len(ends) and ends[j] <= s:
                curr -= 1
                j += 1
            ans = max(ans, curr)
        return ans