class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        x, mid = min([(abs(x), i) for (i, x) in enumerate(A)])
        ans = []
        ans.append(x ** 2)
        i, j = mid - 1, mid + 1
        inf = float('inf')
        while i >= 0 or j < len(A):
            left, right = A[i] if i >= 0 else inf, A[j] if j < len(A) else inf
            if abs(left) <= abs(right):
                ans.append(left ** 2)
                i -= 1
            else:
                ans.append(right ** 2)
                j += 1
        return ans