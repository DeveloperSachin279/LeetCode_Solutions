# Last updated: 7/19/2026, 12:48:04 AM
1class Solution:
2    def reverse(self, x: int) -> int:
3        # Determine the sign of the integer
4        sign = -1 if x < 0 else 1
5        
6        # Convert absolute value to string, reverse it, and convert back to int
7        reversed_x = int(str(abs(x))[::-1]) * sign
8        
9        # Check if the result overflows the 32-bit signed integer range
10        if reversed_x < -2**31 or reversed_x > 2**31 - 1:
11            return 0
12            
13        return reversed_x