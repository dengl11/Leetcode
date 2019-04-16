class Solution:
    def largestSumOfAverages(self, A: List[int], k: int) -> float:
        accSum = [0] * (len(A) + 1)
        for i in range(1, len(A) + 1):
            accSum[i] = accSum[i-1] + A[i-1]
        # dp[i][j]: ans for k = i+1, n = j+1
        dp = [[0]*len(A) for _ in range(k)]

        for i in range(k):
            dp[i][0] = A[0]
        for j in range(1, len(A)):
            dp[0][j] = accSum[j+1]/(j+1)
        for i in range(1, k):
            for j in range(1, len(A)):
                for m in range(i, j+1):
                    dp[i][j] = max(dp[i][j], dp[i-1][m-1] + (accSum[j+1]-accSum[m])/(j+1-m))
        return dp[-1][-1]