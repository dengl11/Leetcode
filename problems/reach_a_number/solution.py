from heapq import heappop, heappush

class Solution:
    def reachNumber(self, target: int) -> int:
        n = 1
        s = 1
        target = abs(target)
        while s < target or (s - target) % 2 == 1:
            n += 1
            s += n
            if s == target: return n
        return n
            