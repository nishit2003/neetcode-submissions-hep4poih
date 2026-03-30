class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        path = set()
        directions = [[0,1],[1,0],[-1,0],[0,-1]]
        res = 0
        def dfs(r,c):
            if (r < 0 or c < 0 or r >= rows or c >= cols or (r,c) in path or grid[r][c] == 0):
                return 0
            
            path.add((r,c))
            area = 1
            for i,j in directions:
                area += dfs(r+i,c+j)
            return area

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1 and (i,j) not in path:
                    res = max(res,dfs(i,j))
        return res
            