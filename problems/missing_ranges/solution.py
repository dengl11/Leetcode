class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        pre = lower
        ans = []
        for x in nums + [upper + 1]:
            if x - pre >= 1:
                if x - pre > 1:
                    ans.append("{}->{}".format(pre, x-1))
                else:
                    ans.append(str(x-1))
            pre = x + 1
        return ans