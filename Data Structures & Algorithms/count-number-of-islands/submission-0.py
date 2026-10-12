class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        dirs = [[1,0],[0,1],[-1,0],[0,-1]]
        ROWS = len(grid)
        COLS = len(grid[0])
        
        def dfs(r,c):
            if r < 0 or c < 0 or r > ROWS-1 or c > COLS-1 or grid[r][c] == '0':
                return
            grid[r][c] = '0'
            for dr, dc in dirs:
                dfs(r+dr,c+dc)
            return

        count = 0
        for i in range(ROWS): 
            for j in range(COLS): 
                if grid[i][j] == '1':
                    dfs(i,j)
                    count += 1

        return count