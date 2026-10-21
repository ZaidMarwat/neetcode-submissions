class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        dirs = [[1,0],[0,1],[-1,0],[0,-1]]
        ROWS, COLS = len(grid), len(grid[0])
        
        q = deque()
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 0:
                    q.append((i,j))
        
        steps = 0
        while q:
            for _ in range(len(q)):
                r,c = q.popleft()
                for dr,dc in dirs:
                    nr,nc = r+dr, c+dc
                    if 0<=nr<ROWS and 0<=nc<COLS and grid[nr][nc] == 2147483647:
                        grid[nr][nc] = steps + 1  # FIX
                        q.append((nr,nc))
            
            steps += 1
        
        
    


