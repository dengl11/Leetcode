from collections import Counter
class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        c = Counter(nums)
        for x in nums:
            while c[x] > 0:
                c[x] -= 1
                y = x + 1
                while c[y] > 0:
                    c[y] -= 1
                    if c[y] >= c[y+1]:
                        break
                    y += 1
                if y - x + 1 < 3: return False
        return True
                