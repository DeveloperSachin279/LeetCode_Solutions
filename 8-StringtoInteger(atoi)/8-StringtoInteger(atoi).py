# Last updated: 9/1/2026, 11:26:29 PM
1class Solution:
2    def isPalindrome(self, x: int) -> bool:
3        # A negative number cannot be a palindrome (e.g., -121 becomes 121-)
4        # If the number ends in 0, it must be 0 to be a palindrome (e.g., 10 is not)
5        if x < 0 or (x % 10 == 0 and x != 0):
6            return False
7            
8        reversed_half = 0
9        
10        # Reverse the second half of the number until it is greater than or equal to the first half
11        while x > reversed_half:
12            reversed_half = reversed_half * 10 + x % 10
13            x //= 10
14            
15        # If the length is even, x == reversed_half
16        # If the length is odd, we can ignore the middle digit by doing reversed_half // 10
17        return x == reversed_half or x == reversed_half // 10