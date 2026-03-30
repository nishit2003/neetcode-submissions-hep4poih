class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows,cols= len(grid), len(grid[0])
        seen = set()
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        
        def dfs(r,c):
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == "0" or (r,c) in seen:
                return 0
            
            seen.add((r,c))

            for i,j in directions:
                dfs(r+i,c+j)
            
            return True

        res = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1" and (i,j) not in seen:
                    dfs(i,j)
                    res +=1
        return res