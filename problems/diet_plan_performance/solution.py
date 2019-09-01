class Solution:
    def dietPlanPerformance(self, cal: List[int], k: int, lower: int, upper: int) -> int:
        curr = sum(cal[:k])
        ans = int(curr > upper) - int(curr < lower)
        for i in range(k, len(cal)):
            curr += cal[i] - cal[i-k]
            ans += int(curr > upper) - int(curr < lower)
        return ans
        