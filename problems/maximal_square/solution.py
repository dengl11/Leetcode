class Solution:
    def maximalSquare(self, M: List[List[str]]) -> int:
        if not M or not M[0]: return 0
        m, n = len(M), len(M[0])
        ans = 0
        rights = [n] * n
        heights = [0] * n
        lefts = [0] * n
        for i in range(m):
            H = [0] * n
            R = [0] * n
            L = [0] * n
            for j in range(n-1, -1, -1):
                if M[i][j] == "1":
                    H[j] = heights[j] + 1
            r = n-1
            for j in range(n-1, -1, -1):
                if M[i][j] == "0":
                    r = j - 1
                    R[j] = n
                else:
                    R[j] = min(rights[j], r)
            l = 0
            for j in range(n):
                if M[i][j] == "0":
                    l = j + 1
                    L[j] = 0
                else:
                    L[j] = max(lefts[j], l)
            for j in range(n):
                ans = max(ans, min(R[j] - L[j] + 1, H[j]) ** 2)
            heights = H
            rights = R
            lefts = L
        return ans
                
            
        