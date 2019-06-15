class Solution:
    def kEmptySlots(self, bulbs: List[int], K: int) -> int:
        days = [-1] * len(bulbs)
        for i, b in enumerate(bulbs, 1):
            days[b-1] = i
        ans = float('inf')
        left = 0
        right = K+1
        for i in range(len(days)):
            if right >= len(days): break
            if days[i] > days[left] and days[i] > days[right]:
                continue
            if i == right:
                ans = min(ans, max(days[left], days[right]))
            left = i
            right = i + K + 1
        return -1 if ans == float('inf') else ans
                