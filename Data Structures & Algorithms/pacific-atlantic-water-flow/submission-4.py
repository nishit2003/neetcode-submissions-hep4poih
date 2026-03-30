class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights:
            return []
        
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        rows,cols = len(heights), len(heights[0])
        pac = [[False] * cols for r in range(rows)]
        atl = [[False] * cols for r in range(rows)]

        def dfs(r,c,seen,prevheight):
            if ((r < 0 or r >= rows) or
                (c < 0 or c >= cols) or
                seen[r][c] or
                heights[r][c] < prevheight):
                return

            seen[r][c] = True
        
            for dr, dc in directions:
                dfs(r+dr,c+dc,seen,heights[r][c])

        for c in range(cols):
            dfs(0,c,pac,heights[0][c])
            dfs(rows-1,c,atl,heights[rows-1][c])
        
        for r in range(rows):
            dfs(r,0,pac, heights[r][0])
            dfs(r,cols-1,atl,heights[r][cols-1])

        res = []
        for r in range(rows):
            for c in range(cols):
                if pac[r][c] and atl[r][c]:
                    res.append([r,c])
        return res
