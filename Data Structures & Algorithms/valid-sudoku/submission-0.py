class Solution:
    def isValidSudoku(self, board):
        seen = set()
        
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == '.':
                    continue
                
                # Define unique string identifiers for row, column, and 3x3 box
                row_key = (r, val)
                col_key = (val, c)
                box_key = (r // 3, c // 3, val)
                
                # If any of these already exist, the board is invalid
                if row_key in seen or col_key in seen or box_key in seen:
                    return False
                
                seen.add(row_key)
                seen.add(col_key)
                seen.add(box_key)
                
        return True