class Solution:
    def subarrayBitwiseORs(self, A: List[int]) -> int:
        frontier = set([0])
        ans = set()
        for x in A:
            frontier = {x | y for y in frontier} | {x}
            ans |= frontier
        return len(ans)
            
        