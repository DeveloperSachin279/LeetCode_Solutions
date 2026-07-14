# Last updated: 7/15/2026, 12:03:23 AM
1class Solution:
2    def findMedianSortedArrays(self, nums1, nums2):
3        # Ensure nums1 is the smaller array
4        if len(nums1) > len(nums2):
5            nums1, nums2 = nums2, nums1
6        
7        m, n = len(nums1), len(nums2)
8        low, high = 0, m
9        
10        while low <= high:
11            i = (low + high) // 2          # partition on nums1
12            j = (m + n + 1) // 2 - i       # partition on nums2
13            
14            # Handle edge cases where partition is at boundaries
15            left1 = nums1[i - 1] if i > 0 else float('-inf')
16            right1 = nums1[i] if i < m else float('inf')
17            left2 = nums2[j - 1] if j > 0 else float('-inf')
18            right2 = nums2[j] if j < n else float('inf')
19            
20            # Valid partition found
21            if left1 <= right2 and left2 <= right1:
22                if (m + n) % 2 == 0:
23                    return (max(left1, left2) + min(right1, right2)) / 2.0
24                else:
25                    return max(left1, left2)
26            # Too far right on nums1 — move left
27            elif left1 > right2:
28                high = i - 1
29            # Too far left on nums1 — move right
30            else:
31                low = i + 1