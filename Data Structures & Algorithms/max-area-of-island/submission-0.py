class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid) , len(grid[0])
        maxArea = 0
        visit = set()


        def dfs(r,c):
            if (r < 0 or r >= rows) or (c < 0 or c >= cols) or grid[r][c] == 0 or (r,c) in visit:
                return 0
            

            area = 1
            visit.add((r,c))
            area += dfs(r+1,c)
            area += dfs(r-1,c)
            area += dfs(r,c+1)
            area += dfs(r,c-1)

            return area

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r,c) not in visit:
                    maxArea = max(maxArea , dfs(r,c))

        return maxArea
