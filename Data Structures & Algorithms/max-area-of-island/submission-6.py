class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [[0,1],[1,0],[-1,0],[0,-1]]
        seen = set()

        
        def dfs(r,c):
            
            if (r<0 or c < 0 or r>= rows or c>=cols or (r,c) in seen or grid[r][c] == 0):
                return 0
            area = 1
            
            seen.add((r,c))
            for dr,dc in directions:
                area += dfs(r+dr,c+dc)
            
            return area

        res = 0 
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r,c) not in seen:
                    res = max(res,dfs(r,c))
        
        return res