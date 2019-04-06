class Solution:
    def minFallingPathSum(self, A: List[List[int]]) -> int:
        arr = A[0]
        n = len(arr)
        for a in A[1:]:
            newArr = [a[i] + min(arr[max(i-1, 0):i+2]) for i in range(n)]
            arr = newArr
        return min(arr)