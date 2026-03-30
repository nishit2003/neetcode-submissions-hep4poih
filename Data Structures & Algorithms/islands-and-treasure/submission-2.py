class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647
        rows, cols = len(grid), len(grid[0])
        directions = [[-1,0],[1,0],[0,-1],[0,1]]

        q = deque()
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    q.append((i,j))

        while q:
            size = len(q)
            for i in range(size):
                node = q.popleft()
                r,c = node
                for dr,dc in directions:
                    nr,nc = r + dr,c+dc
                    if nr< 0 or nr >= rows or nc <0 or nc >= cols or grid[nr][nc] == -1:
                        continue
                    if grid[nr][nc] == INF:
                        grid[nr][nc] = grid[r][c] + 1
                        q.append((nr,nc))

