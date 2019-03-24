class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        for dis in range(1, 4):
            for i in range(len(A) - dis):
                if A[i] == A[i + dis]: return A[i]
                