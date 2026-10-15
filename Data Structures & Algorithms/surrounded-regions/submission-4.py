class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        dirs = [[1,0], [-1,0], [0,1], [0,-1]]
        escape = False
        seen = set()

        def dfs(i, j):
            nonlocal escape
            stack = [(i, j)]

            while stack:
                r, c = stack.pop()

                if not (0 <= r < ROWS and 0 <= c < COLS):
                    escape = True
                    continue

                if (r,c) in seen or board[r][c] == "X":
                    continue

                seen.add((r,c))

                for dr, dc in dirs:
                    stack.append((r+dr, c+dc))

        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == "O":
                    dfs(i,j)

                    if not escape:
                        for r,c in seen:
                            board[r][c] = "X"

                    seen.clear()
                    escape = False