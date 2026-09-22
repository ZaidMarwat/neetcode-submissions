class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        cols = defaultdict(set)
        rows = defaultdict(set)
        squares = defaultdict(set)

        for r in range(len(board)):
            for c in range(len(board[0])):
                val = board[r][c]
                if val == '.':
                    continue
                if val in cols[c] or val in rows[r] or val in squares[(r//3, c//3)]:
                    return False
                
                rows[r].add(val)
                cols[c].add(val)
                squares[(r//3, c//3)].add(val)
        
        return True