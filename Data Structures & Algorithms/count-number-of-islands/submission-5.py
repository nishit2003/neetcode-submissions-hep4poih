class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows,cols = len(grid),len(grid[0])
        path = set()
        directions = [[0,1],[1,0],[-1,0],[0,-1]]

        def dfs(r,c):
            if (r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == '0' or (r,c) in path):
                return False
            
            path.add((r,c))
            for dr,dc in directions:
                if dfs(r+dr,c+dc):
                    return True
                
        cnt = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in path:
                    dfs(r,c)
                    cnt +=1
        return cnt