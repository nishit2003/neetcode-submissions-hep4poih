class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visit = set()
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        res = 0

        def dfs(i,j):
            if i < 0 or j < 0 or i >= rows or j>= cols or grid[i][j]=='0' or (i,j) in visit:
                return 

            visit.add((i,j))
            # res = 0
            for r,c in directions:
                dfs(i+r, j+c)
            
            # return res

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1" and (i, j) not in visit:
                    dfs(i,j)
                    res += 1

        return res
