# Last updated: 7/9/2026, 11:53:07 PM
1class Solution:
2    def twoSum(self, nums: List[int], target: int) -> List[int]:
3        # Dictionary to store the value and its index
4        num_map = {}
5        
6        for i, num in enumerate(nums):
7            # Calculate the difference needed to reach the target
8            complement = target - num
9            
10            # If the complement exists in our map, we've found the pair
11            if complement in num_map:
12                return [num_map[complement], i]
13            
14            # Otherwise, add the current number and its index to the map
15            num_map[num] = i    