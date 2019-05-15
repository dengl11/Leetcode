class Solution(object):
    def profitableSchemes(self, G, P, group, profit):
        """
        :type G: int
        :type P: int
        :type group: List[int]
        :type profit: List[int]
        :rtype: int
        """
        dp = [[0]*(P+1) for _ in range(G+1)]
        dp[0][0] = 1
        for g, p in zip(group, profit):
            for i in range(G, g-1, -1):
                for j in range(P, -1, -1):
                    dp[i][min(p+j, P)] += dp[i-g][j]
        return sum(dp[i][-1] for i in range(G+1)) % (10 ** 9 + 7)
                
            
        