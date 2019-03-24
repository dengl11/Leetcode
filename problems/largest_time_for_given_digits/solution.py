class Solution:
    def largestTimeFromDigits(self, A: List[int]) -> str:
        A.sort()
        for h in range(23, -1, -1):
            d1, d2 = divmod(h, 10)
            for m in range(59, -1, -1):
                d3, d4 = divmod(m, 10)
                if sorted([d1, d2, d3, d4]) == A:
                    return "{}{}:{}{}".format(d1, d2, d3, d4)
        return ""
                
                
                