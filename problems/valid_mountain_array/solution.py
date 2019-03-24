class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        if len(A) < 3 or A[1] <= A[0]: return False
        inc = True
        for i in range(2, len(A)):
            if A[i] == A[i-1]: return False
            newInc = A[i] > A[i-1]
            if not inc and newInc: return False
            inc = newInc
        return not inc 
            
            
        