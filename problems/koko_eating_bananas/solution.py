class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        mi = (sum(piles) - 1 ) // H + 1
        ma = max(piles)
        while mi < ma:
            mid = (mi + ma) // 2
            k = sum((x-1) // mid + 1 for x in piles)
            # print(mi, ma, mid, k)
            if k > H:
                mi = mid + 1
            else:
                ma = mid
                
        return mi
        