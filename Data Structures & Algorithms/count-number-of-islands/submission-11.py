class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [[0,1],[1,0],[-1,0],[0,-1]]
        seen = set()

        def dfs(r,c):
            if r >= rows or r< 0 or c >= cols or c < 0 or (r,c) in seen or grid[r][c] == "0":
                return
            
            seen.add((r,c))
            for dr, dc in directions:
                dfs(r+dr,c+dc)
            return True
            
        res = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in seen:
                    res +=1
                    dfs(r,c)
        return res