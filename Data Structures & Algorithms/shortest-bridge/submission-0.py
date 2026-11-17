class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        dirs = [[0,1],[1,0],[0,-1],[-1,0]]

        q = deque()
        seen = set()

        def dfs(r,c):
            if not (0<=r<ROWS) or not (0<=c<COLS) or grid[r][c] != 1:
                return
            grid[r][c] = 'F'
            q.append((r,c))
            seen.add((r,c))
            for dr,dc in dirs:
                nr,nc = r+dr, c+dc
                dfs(nr,nc)
            return

        found = False
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    dfs(r,c)
                    found = True
                    break
            if found:
                break
        
        count = 0
        while q:
            for _ in range(len(q)):
                r,c = q.popleft()
                for dr,dc in dirs:
                    nr,nc = r+dr, c+dc
                    if 0<=nr<ROWS and 0<=nc<COLS and (nr,nc) not in seen:
                        if grid[nr][nc] == 1:
                            return count
                        q.append((nr,nc))
                        seen.add((nr,nc))
            count += 1
        
        return
        