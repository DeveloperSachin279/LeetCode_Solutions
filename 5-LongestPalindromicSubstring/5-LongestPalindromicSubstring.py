# Last updated: 7/16/2026, 11:51:41 PM
1class Solution:
2    def longestPalindrome(self, s: str) -> str:
3        if not s or len(s) < 1:
4            return ""
5        
6        start = 0
7        end = 0
8        
9        for i in range(len(s)):
10            # Odd length palindrome (single char center)
11            len1 = self.expandAroundCenter(s, i, i)
12            # Even length palindrome (two char center)
13            len2 = self.expandAroundCenter(s, i, i + 1)
14            # Take the longer one
15            max_len = max(len1, len2)
16            
17            # Update if we found a longer palindrome
18            if max_len > end - start:
19                start = i - (max_len - 1) // 2
20                end = i + max_len // 2
21        
22        return s[start:end + 1]
23    
24    def expandAroundCenter(self, s: str, left: int, right: int) -> int:
25        """Expand outward from center and return palindrome length"""
26        while left >= 0 and right < len(s) and s[left] == s[right]:
27            left -= 1
28            right += 1
29        # Length is right - left - 1 (since we overshoot by 1 on each side)
30        return right - left - 1        