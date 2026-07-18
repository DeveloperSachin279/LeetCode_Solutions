# Last updated: 7/19/2026, 12:46:31 AM
1class Solution:
2    def convert(self, s: str, numRows: int) -> str:
3        # If there's only 1 row or the string is shorter than the number of rows,
4        # the zigzag pattern doesn't change the string.
5        if numRows == 1 or numRows >= len(s):
6            return s
7        
8        # Initialize a list of strings to represent each row
9        rows = [""] * numRows
10        current_row = 0
11        going_down = False
12        
13        # Iterate through the string and place each character in the appropriate row
14        for char in s:
15            rows[current_row] += char
16            
17            # If we are at the top or bottom row, reverse the direction
18            if current_row == 0 or current_row == numRows - 1:
19                going_down = not going_down
20            
21            # Move to the next row based on the current direction
22            current_row += 1 if going_down else -1
23            
24        # Combine all rows into a single string
25        return "".join(rows)