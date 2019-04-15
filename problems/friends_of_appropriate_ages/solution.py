from collections import Counter
class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        c = Counter(ages)
        ages = sorted(ages)
        ans = 0
        i = 0
        for j in range(1, len(ages)):
            while i < j and ages[j] >= 2 * (ages[i] - 7):
                i += 1
            ans += (j - i)
        for k, v in c.items():
            if k > 14:
                ans += v * (v-1)//2
        return ans