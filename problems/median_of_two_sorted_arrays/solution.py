class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        if m > n:
            m, n = n, m
            nums1, nums2 = nums2, nums1
        left, right = 0, m
        Mid = (m + n + 1) // 2
        while left <= right:
            mid = (left + right) // 2
            j = Mid - mid
            if mid < m and nums2[j-1] > nums1[mid]:
                left = mid + 1
            elif mid > 0 and nums2[j] < nums1[mid-1]:
                right = mid - 1
            else:
                if mid == 0: leftMax = nums2[j-1]
                elif j == 0: leftMax = nums1[mid-1]
                else: leftMax = max(nums2[j-1], nums1[mid-1])
                
                if (m+n)%2 == 1: return leftMax
                
                if mid >= m: rightMin = nums2[j]
                elif j >= n: rightMin = nums1[mid]
                else: rightMin = min(nums2[j], nums1[mid])
                return (leftMax + rightMin) / 2
                
                