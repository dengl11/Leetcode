class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        i = 1
        while i < len(A) and A[i] == A[i - 1]:
            i += 1
        if i == len(A): return True
        inc = True if A[i] > A[i - 1] else False
        i += 1
        while i < len(A):
            if A[i] != A[i - 1]:
                curr = True if A[i] >= A[i - 1] else False
                if curr != inc: return False
            i += 1
        return True
            