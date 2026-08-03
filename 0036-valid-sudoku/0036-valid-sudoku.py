from collections import defaultdict
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)

        for r in range(9):
            for c in range(9):
                val = board[r][c]

                # Skip empty cell
                if val == '.':
                    continue

                box_key = (r // 3, c // 3)
                # Check if value already seen in row, collumn or 3x3 box
                if val in rows[r] or val in cols[c] or val in boxes[box_key]:
                    return False

                # Register value in sets
                rows[r].add(val)
                cols[c].add(val)
                boxes[box_key].add(val)
        return True
