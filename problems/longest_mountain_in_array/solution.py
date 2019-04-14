class Solution:
    def longestMountain(self, A: List[int]) -> int:
        ans = i = 0
        up = True
        for j, x in enumerate(A[1:], 1):
            if A[j] < A[j-1]:
                if up:
                    if j - i <= 1:
                        i = j
                    else:
                        up = False
            elif A[j] == A[j-1] or not up:
                if not up:
                    ans = max(ans, j - i)
                up = True
                i = j - (A[j] > A[j-1])
        if not up:
            ans = max(ans, len(A) - i)
        return ans if ans >= 3 else 0
                
        