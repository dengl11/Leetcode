class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        l1, l2 = len(s1), len(s2)
        s1 = [ord(c) for c in s1]
        s2 = [ord(c) for c in s2]
        dp = [[0] * (l2+1) for _ in range(l1+1)]
        
        for i in range(1, l1+1):
            dp[i][0] = dp[i-1][0] + s1[i-1]
        
        for j in range(1, l2+1):
            dp[0][j] = dp[0][j-1] +s2[j-1]
            
        for i in range(1, l1+1):
            for j in range(1, l2+1):
                if s1[i-1] == s2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(s1[i-1] + dp[i-1][j], s2[j-1] + dp[i][j-1])
        return dp[-1][-1]
        