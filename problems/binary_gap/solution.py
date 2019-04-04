class Solution:
    def binaryGap(self, N: int) -> int:
        s = bin(N)[2:]
        pre = -1
        ans = 0
        for i, c in enumerate(s):
            if c == '0': continue
            if pre < 0:
                pre = i
            else:
                ans = max(ans, i - pre)
                pre = i
        return ans
        