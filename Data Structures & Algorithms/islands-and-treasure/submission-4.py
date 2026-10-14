class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        dirs = [[1,0],[-1,0],[0,1],[0,-1]]
        ROWS = len(grid)
        COLS = len(grid[0])
        
        q = deque()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r,c))
        
        steps = 1
        while q:
            for _ in range(len(q)):
                r,c = q.popleft()

                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if 0<=nr<ROWS and 0<=nc<COLS and grid[nr][nc] == 2147483647:
                        q.append((nr,nc))
                        grid[nr][nc] = steps
            steps += 1
        

