from bisect import bisect_left
class Solution:
    def prevPermOpt1(self, A: List[int]) -> List[int]:
        stack = []
        for i in range(len(A)-1, -1, -1):
            x = A[i]
            if not stack or stack[-1] >= x:
                stack.append(x)
            else:
                stack.reverse()
                j = bisect_left(stack, x) + i 
                while j - 1 > 0 and A[j] == A[j-1]:
                    j -= 1
                A[i], A[j] = A[j], A[i]
                return A
        return A
        