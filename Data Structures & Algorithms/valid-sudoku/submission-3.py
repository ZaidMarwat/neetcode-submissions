class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        rows = [0] * 9
        cols = [0] * 9
        squares = [0] * 9

        for r in range(len(board)):
            for c in range(len(board[0])):
                val = board[r][c]
                if val == '.':
                    continue
                mask = 1 << (int(val) - 1)

                if rows[r] & mask:
                    return False
                if cols[c] & mask:
                    return False
                if squares[r//3*3 + c//3] & mask:
                    return False
                
                rows[r] |= mask
                cols[c] |= mask
                squares[r//3*3 + c//3] |= mask
        
        return True
