# Last updated: 9/1/2026, 11:28:19 PM
class Solution:
    def isPalindrome(self, x: int) -> bool:
        # A negative number cannot be a palindrome (e.g., -121 becomes 121-)
        # If the number ends in 0, it must be 0 to be a palindrome (e.g., 10 is not)
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
            
        reversed_half = 0
        
        # Reverse the second half of the number until it is greater than or equal to the first half
        while x > reversed_half:
            reversed_half = reversed_half * 10 + x % 10
            x //= 10
            
        # If the length is even, x == reversed_half
        # If the length is odd, we can ignore the middle digit by doing reversed_half // 10
        return x == reversed_half or x == reversed_half // 10