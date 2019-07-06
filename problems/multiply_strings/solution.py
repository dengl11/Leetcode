class Solution:
    def multiply(self, nums1: str, nums2: str) -> str:
        nums1 = [int(x) for x in nums1]
        nums2 = [int(x) for x in nums2]
        ans = 0
        order = 1
        for i in nums1[::-1]:
            c = order
            for j in nums2[::-1]:
                ans += i * j * c
                c *= 10
            order *= 10
        return str(ans)
        