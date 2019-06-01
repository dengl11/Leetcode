class Solution:
    def findIntegers(self, num: int) -> int:
        def valid(s):
            for i in range(1, len(s)):
                if s[i] == '1' and s[i-1] == '1':
                    return False
            return True
        pos = [] # pos of 1's bit in nums
        for j in range(32):
            if num & (1 << j):
                pos.append(j)
        
        dp = [1, 2, 3] # dp[i]: the number of cases for i digits
        while len(dp) <= pos[-1]:
            dp.append(dp[-1] + dp[-2])
            
        ans = 0
        pre = 10000
        while pos:
            i = pos.pop()
            ans += dp[i]
            if pre - i == 1: # two consecutive 1`s, stop here
                break
            else:
                pre = i
        return ans + int(valid(bin(num)[2:]))
            
            
        