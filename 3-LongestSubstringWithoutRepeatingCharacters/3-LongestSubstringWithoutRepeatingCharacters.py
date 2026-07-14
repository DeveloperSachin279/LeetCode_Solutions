# Last updated: 7/14/2026, 11:01:43 PM
1class Solution:
2    def lengthOfLongestSubstring(self, s: str) -> int:
3        char_set = set()
4        left = 0
5        max_length = 0
6
7        for right in range(len(s)):
8            # If duplicate found, shrink window from left
9            while s[right] in char_set:
10                char_set.remove(s[left])
11                left += 1
12            # Add current character and update max
13            char_set.add(s[right])
14            max_length = max(max_length, right - left + 1)
15
16        return max_length   