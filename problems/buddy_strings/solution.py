class Solution:
    def buddyStrings(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if len(A) != len(B): return False
        x1 = x2 = -1
        for i,c in enumerate(A):
            if A[i] == B[i]: continue
            if x1 < 0:
                x1 = i
            else:
                if x2 >= 0: return False
                x2 = i
        if x1 < 0 and x2 < 0:
            return len(set(A)) < len(A)
        if x1 >= 0 and x2 < 0:
            return False
        return A[x1] == B[x2] and A[x2] == B[x1]