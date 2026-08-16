class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return

        rows, cols = len(board), len(board[0])

        def count_live_neighbors(r, c):
            live_count = 0
            for dr in (-1, 0, 1):
                for dc in (-1, 0, 1):
                    if dr == 0 and dc == 0:
                        continue
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols:
                        # Cells with values 1 or 2 were originally live
                        if board[nr][nc] in (1, 2):
                            live_count += 1
            return live_count

        # Step 1: Apply rules and store intermediate states
        for r in range(rows):
            for c in range(cols):
                neighbors = count_live_neighbors(r, c)

                if board[r][c] == 1:
                    if neighbors < 2 or neighbors > 3:
                        board[r][c] = 2  # Live -> Dead
                else:
                    if neighbors == 3:
                        board[r][c] = 3  # Dead -> Live

        # Step 2: Convert intermediate states to final values
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 2:
                    board[r][c] = 0
                elif board[r][c] == 3:
                    board[r][c] = 1