from bisect import bisect_left as bl, bisect_right as br
class Solution:
    def fallingSquares(self, positions: List[List[int]]) -> List[int]:
        ans, xs, hs = [], [0], [0]
        for (x, h) in positions:
            i, j = br(xs, x), bl(xs, x+h)
            H = max(hs[max(i-1, 0):j], default = 0) + h
            xs[i:j] = [x, x + h]
            hs[i:j] = [H, hs[j - 1]]
            ans.append(H)
            if len(ans) > 1:
                ans[-1] = max(ans[-1], ans[-2])
        return ans
            
            