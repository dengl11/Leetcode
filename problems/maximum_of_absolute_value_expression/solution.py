class Solution:
    def maxAbsValExpr(self, arr1: List[int], arr2: List[int]) -> int:
        ans = 0
        for s1 in [1, -1]:
            for s2 in [1, -1]:
                mi = s1 * arr1[0] + s2 * arr2[0] + 0
                for i in range(len(arr1)):
                    curr = s1 * arr1[i] + s2 * arr2[i] + i
                    ans = max(ans, curr - mi)
                    mi = min(mi, curr)
        return ans
                