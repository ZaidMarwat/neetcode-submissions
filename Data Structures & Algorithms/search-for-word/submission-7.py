class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        dirs = [[0,1],[1,0],[0,-1],[-1,0]]
        s = set()
        ROWS, COLS = len(board), len(board[0])

        def dfs(r,c,i):
            if r<0 or r>=ROWS or c<0 or c>=COLS or i>=len(word):
                return False
            if board[r][c] != word[i]:
                return False
            if i == len(word)-1:
                return True
            
            s.add((r,c))

            for dr,dc in dirs:
                nr,nc = r+dr,c+dc
                if (nr,nc) not in s and dfs(nr, nc, i+1):
                    return True
            s.remove((r,c))

            return False
        
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == word[0]:
                    if dfs(r,c,0):
                        return True
        
        return False


                