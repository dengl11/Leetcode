class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        pre, curr = {(0, 0): 0}, {}
        for i, h in enumerate(houses):
            choices = [h] if h != 0 else list(range(1, n+1))
            for c in choices:
                for (pre_c, pre_block), pre_cost in pre.items():
                    curr_block = pre_block + int(pre_c != c)
                    if curr_block > target: continue
                    curr[c, curr_block] = min(pre_cost + (0 if h > 0 else cost[i][c-1]), curr.get((c, curr_block), float('inf')))
            pre, curr = curr, {}
        return min([c for (pre_c, pre_block), c in pre.items() if pre_block == target] or [-1])
                
                