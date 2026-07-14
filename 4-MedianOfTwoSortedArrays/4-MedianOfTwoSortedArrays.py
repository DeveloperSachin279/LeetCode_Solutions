# Last updated: 7/15/2026, 12:14:17 AM
class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        # Ensure nums1 is the smaller array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        m, n = len(nums1), len(nums2)
        low, high = 0, m
        
        while low <= high:
            i = (low + high) // 2          # partition on nums1
            j = (m + n + 1) // 2 - i       # partition on nums2
            
            # Handle edge cases where partition is at boundaries
            left1 = nums1[i - 1] if i > 0 else float('-inf')
            right1 = nums1[i] if i < m else float('inf')
            left2 = nums2[j - 1] if j > 0 else float('-inf')
            right2 = nums2[j] if j < n else float('inf')
            
            # Valid partition found
            if left1 <= right2 and left2 <= right1:
                if (m + n) % 2 == 0:
                    return (max(left1, left2) + min(right1, right2)) / 2.0
                else:
                    return max(left1, left2)
            # Too far right on nums1 — move left
            elif left1 > right2:
                high = i - 1
            # Too far left on nums1 — move right
            else:
                low = i + 1