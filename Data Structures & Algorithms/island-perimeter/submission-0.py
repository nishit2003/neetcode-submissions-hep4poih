class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid),len(grid[0])
        visit = set()
        directions = [[1,0],[0,1],[-1,0],[0,-1]]

        def dfs(r,c):
            if r < 0 or c < 0 or r>=rows or c>= cols or grid[r][c] == 0:
                return 1

            if (r,c) in visit:
                return 0
            
            visit.add((r,c))
            perim = 0
            for dr, dc in directions:
                perim+=dfs(r+dr,c+dc)
            return perim
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]:
                    return dfs(r,c)
        return 0
            