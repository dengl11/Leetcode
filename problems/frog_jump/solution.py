from collections import defaultdict
class Solution:
    def canCross(self, stones: List[int]) -> bool:
        reachable = defaultdict(set)
        S = set(stones)
        if stones[0] + 1 not in S: return False
        reachable[stones[0] + 1] = {stones[0]}
        for i in stones[1:]:
            for pre in reachable[i]:
                d = i - pre
                if d + i in S:
                    reachable[d+i].add(i)
                if d + i + 1 in S:
                    reachable[d+i+1].add(i)
                if d > 1 and d + i - 1 in S:
                    reachable[d+i-1].add(i)
        return len(reachable[stones[-1]]) > 0
        