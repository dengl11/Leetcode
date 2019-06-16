class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        m, n = len(str1), len(str2)
        dp = [[0]*(n+1) for _ in range(m+1)]
        for i in range(m):
            for j in range(n):
                if str1[i] == str2[j]:
                    dp[i+1][j+1] = dp[i][j] + 1
                else:
                    dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])
        shared = []
        i = m - 1
        j = n - 1
        # print(dp)
        while i >= 0 and j >= 0:
            if str1[i] == str2[j]:
                shared.append(str1[i])
                i -= 1
                j -= 1
            else:
                if dp[i+1][j+1] == dp[i+1][j]:
                    j -= 1
                else:
                    i -= 1
        ans = ""
        i = j = 0
        # print(shared)
        while i < m or j < n:
            if not shared:
                ans += str1[i:] + str2[j:]
                i = m
                j = n
            else:
                c = shared.pop()
                while i < m and str1[i] != c:
                    ans += str1[i]
                    i += 1
                while j < n and str2[j] != c:
                    ans += str2[j]
                    j += 1
                ans += c
                i += 1
                j += 1
        return ans