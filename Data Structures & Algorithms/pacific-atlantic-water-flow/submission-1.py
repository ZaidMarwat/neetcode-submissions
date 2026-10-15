class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        dirs = [[0,1],[1,0],[-1,0],[0,-1]]
        ROWS, COLS = len(heights), len(heights[0])
        qp = deque()
        qa = deque()
        pac = [[False] * COLS for _ in range(ROWS)]
        atl = [[False] * COLS for _ in range(ROWS)]
        for i in range(ROWS):
            for j in range(COLS):
                if i == 0 or j == 0:
                    pac[i][j] = True
                    qp.append([i,j])
                if i == ROWS-1 or j == COLS-1:
                    atl[i][j] = True
                    qa.append([i,j])

        while qp:
            for _ in range(len(qp)):
                r, c = qp.popleft() 
                for dr, dc in dirs:
                    nr, nc = r+dr, c+dc
                    if 0<=nr<ROWS and 0<=nc<COLS and heights[r][c] <= heights[nr][nc] and not pac[nr][nc]:
                        pac[nr][nc] = True
                        qp.append((nr,nc))
        while qa:
            for _ in range(len(qa)):
                r, c = qa.popleft() 
                for dr, dc in dirs:
                    nr, nc = r+dr, c+dc
                    if 0<=nr<ROWS and 0<=nc<COLS and heights[r][c] <= heights[nr][nc] and not atl[nr][nc]:
                        atl[nr][nc] = True
                        qa.append((nr,nc))
        
        res = []
        for i in range(ROWS):
            for j in range(COLS):
                if pac[i][j] and atl[i][j]:
                    res.append([i,j])

        return res


