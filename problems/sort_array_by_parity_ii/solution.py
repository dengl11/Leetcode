from collections import deque
class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        odds, evens = deque(), deque() # positions that have index as odd or even
        for i, x in enumerate(A):
            if i % 2 == x % 2: continue
            pre = None
            if x%2 == 1: # odd value, swap with odds
                if odds:
                    pre = odds.popleft()
                else:
                    evens.append(i)
            else:
                if evens:
                    pre = evens.popleft()
                else:
                    odds.append(i)
            if pre is not None:
                A[pre], A[i] = x, A[pre]
        return A
                