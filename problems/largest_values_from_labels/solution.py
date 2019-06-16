from collections import Counter
class Solution:
    def largestValsFromLabels(self, values: List[int], labels: List[int], num_wanted: int, use_limit: int) -> int:
        ans = 0
        used = 0
        counter = Counter()
        for v, l in sorted(zip(values, labels), reverse = True):
            if counter[l] >= use_limit: continue
            ans += v
            counter[l] += 1
            used += 1
            if used >= num_wanted: return ans
        return ans
            