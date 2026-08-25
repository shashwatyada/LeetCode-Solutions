class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return

        rows, cols = len(board), len(board[0])

        def dfs(r, c):
            # Out of bounds or not an unvisited 'O'
            if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != 'O':
                return
            
            # Mark the cell as safe/visited
            board[r][c] = 'T'

            # Visit all 4 orthogonal neighbors
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        # 1. Run DFS from all border 'O's
        for r in range(rows):
            for c in range(cols):
                # Check if the cell is on any of the 4 borders
                if r in (0, rows - 1) or c in (0, cols - 1):
                    if board[r][c] == 'O':
                        dfs(r, c)

        # 2. Flip surrounded 'O's to 'X', and restore 'T's back to 'O'
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O':
                    board[r][c] = 'X'  # Surrounded
                elif board[r][c] == 'T':
                    board[r][c] = 'O'  # Safe