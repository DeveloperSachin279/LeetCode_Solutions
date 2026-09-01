# Last updated: 9/2/2026, 12:00:00 AM
1class Solution:
2    def maxArea(self, height: list[int]) -> int:
3        left = 0
4        right = len(height) - 1
5        max_area = 0
6        
7        while left < right:
8            current_width = right - left
9            current_height = min(height[left], height[right])
10            
11            current_area = current_width * current_height
12            max_area = max(max_area, current_area)
13            
14            if height[left] < height[right]:
15                left += 1
16            else:
17                right -= 1
18                
19        return max_area