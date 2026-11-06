class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        
        ROWS,COLS = len(grid), len(grid[0])
        dirs = [[0,1],[1,0],[0,-1],[-1,0]]

        minHeap = [(grid[0][0],0,0)]
        seen = {(0,0)}
        res = 0
        while minHeap:
            val,r,c = heapq.heappop(minHeap)
            res = max(res, grid[r][c])
            if r == ROWS-1 and c == COLS-1:
                return res
            for dr,dc in dirs:
                nr,nc = r+dr, c+dc
                if 0<=nr<ROWS and 0<=nc<COLS and (nr,nc) not in seen:
                    heapq.heappush(minHeap, (grid[nr][nc],nr,nc))
                    seen.add((nr,nc))
            
            print(minHeap[0])


