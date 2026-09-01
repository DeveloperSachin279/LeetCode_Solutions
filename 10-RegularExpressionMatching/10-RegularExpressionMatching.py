# Last updated: 9/1/2026, 11:58:52 PM
1class Solution:
2    def isMatch(self, s: str, p: str) -> bool:
3        # dp[i][j] will be True if the substring s[i:] matches the pattern p[j:]
4        dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
5        
6        # Base case: an empty string matches an empty pattern
7        dp[len(s)][len(p)] = True
8        
9        # Build the table from the bottom-right back to the top-left (dp[0][0])
10        for i in range(len(s), -1, -1):
11            # We don't check j=len(p) because an empty pattern can't match a non-empty string
12            for j in range(len(p) - 1, -1, -1):
13                
14                # Check if the current characters match (or if the pattern has a wildcard '.')
15                first_match = i < len(s) and p[j] in {s[i], '.'}
16                
17                # Check if the NEXT character in the pattern is a '*'
18                if j + 1 < len(p) and p[j+1] == '*':
19                    # We have two choices when dealing with a '*':
20                    # 1. Zero matches: We ignore the current character and the '*' in the pattern (move j by 2).
21                    # 2. One or more matches: If `first_match` is True, we move forward in the string (move i by 1) but keep the '*' to match more characters.
22                    dp[i][j] = dp[i][j+2] or (first_match and dp[i+1][j])
23                else:
24                    # If there's no '*', we must have a direct match, and then we move forward in both the string and the pattern.
25                    dp[i][j] = first_match and dp[i+1][j+1]
26                    
27        # The result for the entire string and pattern is stored at dp[0][0]
28        return dp[0][0]