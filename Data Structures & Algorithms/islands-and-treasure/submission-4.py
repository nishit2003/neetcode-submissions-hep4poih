class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647
        rows,cols = len(grid), len(grid[0])
        directions = [[0,1],[1,0],[-1,0],[0,-1]]

        q = deque()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r,c))
        
        while q:
            size = len(q)
            for i in range(size):
                r,c = q.popleft()
                for dr,dc in directions:
                    nr,nc = r+dr,c+dc
                    if nr < 0 or nr >= rows or nc < 0 or nc >= cols or grid[nr][nc] != INF:
                        continue
                    grid[nr][nc] = 1 + grid[r][c]
                    q.append((nr,nc))