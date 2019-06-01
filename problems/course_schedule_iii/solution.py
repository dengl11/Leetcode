from heapq import heappop, heappush
class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        # sort by expiration date
        courses.sort(key = lambda x: x[1])
        ans = 0
        durations = []
        t = 0
        for d, e in courses:
            t += d
            heappush(durations, -d)
            ans += 1
            if t > e:
                t += heappop(durations)
                ans -= 1
        return ans
            
            
            
        