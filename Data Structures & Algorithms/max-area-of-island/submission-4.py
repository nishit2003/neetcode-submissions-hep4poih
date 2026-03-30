class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid),len(grid[0])
        directions =[[0,1],[-1,0],[0,-1],[1,0]]
        visit = set()

        def dfs(r,c):
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] != 1 or (r,c) in visit:
                return 0
            
            area = 1
            visit.add((r,c))
            for dr,dc in directions:
                area+=dfs(r+dr,c+dc)
            # visit.remove((r,c))
            
            return area
        
        MaxArea = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    MaxArea = max(MaxArea, dfs(r,c))
        return MaxArea