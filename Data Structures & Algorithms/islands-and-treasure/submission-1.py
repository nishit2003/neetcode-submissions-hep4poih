class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid),len(grid[0])
        directions = [[-1,0],[0,1],[0,-1],[1,0]]
        INF = 2147483647
        q = deque()
        seen = set()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r,c))

        while q:
            size = len(q)
            for i in range(size):
                node = q.popleft()
                r,c = node
                for dr,dc in directions:
                    nr,nc = r+dr, c+dc
                    if nr<0 or nc<0 or nr>=rows or nc>=cols or grid[nr][nc] == -1 or (r,c) in seen:
                        continue
                    if grid[nr][nc] == INF:
                        grid[nr][nc] = grid[r][c] + 1
                        q.append((nr,nc))
            