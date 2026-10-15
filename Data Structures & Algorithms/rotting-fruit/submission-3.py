class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        dirs = [[1,0],[-1,0],[0,1],[0,-1]]
        ROWS = len(grid)
        COLS = len(grid[0])

        q = deque()
        ones = 0
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 2:
                    q.append((i,j))
                if grid[i][j] == 1:
                    ones += 1
        
        mins = 0
        while ones > 0 and q:
            for _ in range(len(q)):
                r,c = q.popleft()
                for dr, dc in dirs:
                    nr, nc = r+dr, c+dc
                    if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == 1:
                        q.append((nr,nc))
                        grid[nr][nc] = 2
                        ones -= 1
            
            mins += 1
        
        return mins if not ones else -1
                    
