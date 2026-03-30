class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        path = set()
        directions = [[0,1],[1,0],[-1,0],[0,-1]]

        def dfs(r,c):
            if (r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] != 1 or (r,c) in path):
                return False
            
            path.add((r,c))
            
            area = 1
            for dr, dc in directions:
                    area += dfs(r+dr,c+dc)
            return area

        res = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    res = max(res,dfs(r,c))
        return res