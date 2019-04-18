class Solution:
    def numTilings(self, N: int) -> int:
        ans = [(0, 0), (1, 1), (2, 1)]
        while len(ans)-1 < N:
            curr = ans[-1][0] + ans[-2][0]
            curr += 2 * (ans[-2][1] + ans[-3][1])
            ans.append([curr, ans[-1][0] + ans[-2][1]])
        return ans[N][0] % (10**9 + 7)
        