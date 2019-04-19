class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        ans = 0
        need = -1
        for j, x in enumerate(arr):
            if j > need:
                ans += 1
            need = max(x, need)
        return ans
            
            
        