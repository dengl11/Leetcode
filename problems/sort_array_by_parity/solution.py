class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        i, j = 0, len(A) - 1
        while i < j:
            while i < j and A[i] % 2 == 0:
                i += 1
            while j > i and A[j] % 2 == 1:
                j -= 1
            A[i], A[j] = A[j], A[i]
            i += 1
            j -= 1
        return A
        