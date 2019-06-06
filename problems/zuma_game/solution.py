from collections import Counter
from functools import lru_cache
class Solution:
    def findMinStep(self, board: str, hand: str) -> int:
        inf = float('inf')
        @lru_cache(None)
        def dfs(board, hand):
            # print(board, hand)
            if not hand: return inf if board else 0
            if not board: return 0
            ans = inf
            counter = Counter(hand)
            for i, c in enumerate(board):
                if c not in counter: continue
                if i > 0 and c == board[i-1]: continue
                counter[c] -= 1
                # print("Using: ", c)
                _hand = "".join(k*counter[k] for k in sorted(counter.keys()))
                _board = board[:i] + c + board[i:]
                merging = True
                while merging:
                    merging = False
                    for i in range(len(_board) - 2):
                        j = i+1
                        while j < len(_board) and _board[j] == _board[j-1]:
                            j += 1
                        if j - i >= 3:
                            _board = _board[:i] + _board[j:]
                            merging = True
                            break
                curr = dfs(_board, _hand)
                # print("curr: _board = {}, _hand = {}, curr = {}".format(_board, _hand, curr))
                ans = min(ans, 1 + curr)
                counter[c] += 1  
            return ans
    
        ans = dfs(board, "".join(sorted(hand)))
        return ans if ans != inf else -1
                    
                
                
            