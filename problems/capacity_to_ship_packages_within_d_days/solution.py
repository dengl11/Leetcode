class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        left, right = max(weights), sum(weights)
        while left < right:
            mid = (left + right) // 2
            need = 1
            curr = 0
            for w in weights:
                if curr + w > mid:
                    need += 1
                    curr = 0
                curr += w
            if need > D: left = mid + 1
            else:
                right = mid
        return left