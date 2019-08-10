class Solution:
    def minSwaps(self, data: List[int]) -> int:
        ones = sum(data)
        window = sum(data[:ones])
        ans = ones - window
        for i in range(ones, len(data)):
            window += (data[i] - data[i-ones])
            ans = min(ans, ones - window)
        return ans
            
        