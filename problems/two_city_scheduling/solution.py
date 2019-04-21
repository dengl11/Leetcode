class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        pairs = sorted(costs, key = lambda x: -abs(x[0]-x[1]))
        na = nb = len(costs)//2
        ans = 0
        for pa, pb in pairs:
            if pa < pb:
                if na > 0: 
                    ans += pa
                    na -= 1
                else:
                    ans += pb
            else:
                if nb > 0:
                    ans += pb
                    nb -= 1
                else:
                    ans += pa
        return ans