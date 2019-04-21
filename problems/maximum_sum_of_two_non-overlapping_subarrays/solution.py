class Solution:
    def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:
        endM, endL, startM, startL = [-1]*len(A), [-1]*len(A), [-1]*len(A), [-1]*len(A)
        currM = sum(A[:M])
        currL = sum(A[:L])
        endM[M-1] = currM
        endL[L-1] = currL
        for i, a in enumerate(A):
            if i >= M:
                currM += a - A[i-M]
                endM[i] = max(endM[i-1], currM)
            if i >= L:
                currL += a - A[i-L]
                endL[i] = max(endL[i-1], currL)
        A.reverse()
        currM = sum(A[:M])
        currL = sum(A[:L])
        startM[~(M-1)] = currM
        startL[~(L-1)] = currL
        for i, a in enumerate(A):
            if i >= M:
                currM += a - A[i-M]
                startM[~i] = max(startM[~(i-1)], currM)
            if i >= L:
                currL += a - A[i-L]
                startL[~i] = max(startL[~(i-1)], currL)
        ans = 0
        for i in range(len(A)-1):
            if startM[i+1] > 0 and endL[i] > 0:
                ans = max(startM[i+1] + endL[i], ans)
            if startL[i+1] > 0 and endM[i] > 0:
                ans = max(startL[i+1] + endM[i], ans)
        return ans
            
            
        