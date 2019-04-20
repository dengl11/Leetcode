from collections import Counter
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        counter = Counter(nums)
        if not counter: return 0
        pairs = sorted(counter.items())
        keep = pairs[0][0] * pairs[0][1]
        removed = 0
        for i in range(1, len(pairs)):
            curr = pairs[i][0] * pairs[i][1]
            if pairs[i][0] > pairs[i-1][0]+1:
                removed = max(keep, removed)
                keep = removed + curr
            else:
                keep, removed = removed + curr, max(keep, removed)
        return max(keep, removed)
                
            