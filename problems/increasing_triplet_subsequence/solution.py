class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) < 3: return False
        lmins = [nums[0]]
        rmaxs = [nums[-1]]
        for x in nums[1:-1]:
            lmins.append(min(lmins[-1], x))
        for y in nums[-2:0:-1]:
            rmaxs.append(max(rmaxs[-1], y))
        # print(lmins, rmaxs[::-1])
        return any(l < x < r for (l,x,r) in zip(lmins[1:], nums[1:-1], rmaxs[:0:-1]))