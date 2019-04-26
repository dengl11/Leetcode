from heapq import heappush, heappop
class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        q = [(0, tuple(needs))]
        while q:
            p, state = heappop(q)
            if max(state) == 0: return p
            for s in special:
                if any(s[i] > state[i] for i in range(len(state))): continue
                new_state = tuple(state[i] - s[i] for i in range(len(state)))
                heappush(q, ((p + s[-1], new_state)))
            heappush(q, (p + sum(x * y for (x, y) in zip(price, state)), tuple(0 for i in range(len(state)))))
