"""
# Definition for an Interval.
class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
from heapq import heappop, heappush
class Solution:
    def employeeFreeTime(self, schedule: 'list<list<Interval>>') -> 'list<Interval>':
        schedule = [[(x.start, x.end) for x in s[::-1]] for s in schedule if s]
        ans = []
        q = []
        for i, s in enumerate(schedule):
            heappush(q, (s.pop(), i))
        pre = -1
        while q:
            (s, t), i = heappop(q)
            if pre >= 0 and s > pre:
                ans.append(Interval(pre, s))
            pre = max(pre, t)
            if schedule[i]:
                heappush(q, (schedule[i].pop(), i))
                
        return ans
                
            
            
            