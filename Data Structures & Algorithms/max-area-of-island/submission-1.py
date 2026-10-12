class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        dirs = [[1,0],[-1,0],[0,1],[0,-1]]
        ROWS = len(grid)
        COLS = len(grid[0])

        def dfs(r,c):
            if r<0 or c<0 or r>ROWS-1 or c>COLS-1 or grid[r][c] == 0:
                return 0
            
            grid[r][c] = 0
            count = 0
            for dr, dc in dirs:
                count += dfs(r+dr, c+dc)
            
            return 1 + count
        
        res = 0
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    res = max(res, dfs(i,j))
            
        return res