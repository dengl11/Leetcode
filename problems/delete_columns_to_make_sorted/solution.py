class Solution:
    def minDeletionSize(self, A: List[str]) -> int:
        deletions = 0
        if not A or not A[0]: return 0
        rows, colns = len(A), len(A[0])
        for col in range(colns): # for each column
            for row in range(rows-1): # for each row
                if A[row][col] > A[row+1][col]:
                    deletions += 1
                    break
        return deletions
                
            