class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        sa = sorted(arr)
        ans, s1, s2 = 0, 0, 0
        for x, y in zip(sa, arr):
            s1 += x
            s2 += y
            if s1 == s2: ans += 1
        return ans