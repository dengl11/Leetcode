class Solution:
    def shortestToChar(self, S: str, C: str) -> List[int]:
        n = len(S)
        ans = [n] * n
        
        for k in range(2):
            stack = []
            if k == 1: S = S[::-1]
            for ii, c in enumerate(S):
                if c != C:
                    stack.append(ii)
                else:
                    if k == 0:
                        ans[ii] = 0
                    i = 1
                    while stack:
                        idx = stack.pop()
                        idx = idx if k == 0 else n-1-idx
                        ans[idx] = min(ans[idx], i)
                        i += 1
        return ans
