class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        dirs = [[0,1],[1,0],[0,-1],[-1,0]]

        diridx = 0
        res = []
        r,c = 0,0
        seen = set()
        ROWS, COLS = len(matrix), len(matrix[0])
        count = 0
        while count < ROWS*COLS:
            while 0<=r<ROWS and 0<=c<COLS and (r,c) not in seen:
                seen.add((r,c))
                res.append(matrix[r][c])
                r,c = r+dirs[diridx % 4][0], c+dirs[diridx % 4][1]
            r,c = r-dirs[diridx % 4][0], c-dirs[diridx % 4][1]
            diridx += 1
            r,c = r+dirs[diridx % 4][0], c+dirs[diridx % 4][1]
            count += 1
        
        return res