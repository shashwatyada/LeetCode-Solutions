class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        # Edge Case: If only one row or s fits within numRows, output is unchanged
        if numRows == 1 or numRows >= len(s):
            return s

        # Create an array of strings for each row
        rows = ['']  * numRows
        curr_row = 0
        going_down = False

        for char in s:
            rows[curr_row] += char 

            # Reverse direction when reaching top or bottom row 
            if curr_row == 0 or curr_row == numRows -1:
                going_down = not going_down

            curr_row += 1 if going_down else -1
        
        # Concatenate all rows
        return "".join(rows)