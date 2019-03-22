class Solution:
    def largestPerimeter(self, A: List[int]) -> int:
        A.sort()
        while len(A) >= 3:
            if A[-1] >= A[-2] + A[-3]:
                A.pop()
                continue
            return sum(A[-3:])
        return 0