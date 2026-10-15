class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        dirs = [[1,0],[-1,0],[0,1],[0,-1]]

        def capture():
            q = deque()
            for r in range(ROWS):
                q.append((r,0)) if board[r][0] == "O" else None
                q.append((r,COLS-1)) if board[r][COLS-1] == "O" else None
            for c in range(COLS):
                q.append((0,c)) if board[0][c] == "O" else None
                q.append((ROWS-1,c)) if board[ROWS-1][c] == "O" else None

            while q:
                r,c = q.popleft()
                board[r][c] = "T"
                for dr,dc in dirs:
                    nr,nc = r+dr, c+dc
                    if 0<=nr<ROWS and 0<=nc<COLS and board[nr][nc] == "O":
                        q.append((nr,nc))

        capture()
        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "T":
                    board[i][j] = "O"