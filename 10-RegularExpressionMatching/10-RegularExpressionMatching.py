# Last updated: 9/1/2026, 11:28:21 PM
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # dp[i][j] will be True if the substring s[i:] matches the pattern p[j:]
        dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
        
        # Base case: an empty string matches an empty pattern
        dp[len(s)][len(p)] = True
        
        # Build the table from the bottom-right back to the top-left (dp[0][0])
        for i in range(len(s), -1, -1):
            # We don't check j=len(p) because an empty pattern can't match a non-empty string
            for j in range(len(p) - 1, -1, -1):
                
                # Check if the current characters match (or if the pattern has a wildcard '.')
                first_match = i < len(s) and p[j] in {s[i], '.'}
                
                # Check if the NEXT character in the pattern is a '*'
                if j + 1 < len(p) and p[j+1] == '*':
                    # We have two choices when dealing with a '*':
                    # 1. Zero matches: We ignore the current character and the '*' in the pattern (move j by 2).
                    # 2. One or more matches: If `first_match` is True, we move forward in the string (move i by 1) but keep the '*' to match more characters.
                    dp[i][j] = dp[i][j+2] or (first_match and dp[i+1][j])
                else:
                    # If there's no '*', we must have a direct match, and then we move forward in both the string and the pattern.
                    dp[i][j] = first_match and dp[i+1][j+1]
                    
        # The result for the entire string and pattern is stored at dp[0][0]
        return dp[0][0]