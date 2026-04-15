class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        memo = {}
        
        def dfs(r, c):
            if (r, c) in memo:
                return memo[(r, c)]
            
            res = 1
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and matrix[nr][nc] > matrix[r][c]:
                    res = max(res, 1 + dfs(nr, nc))
            
            memo[(r, c)] = res
            return res

        ans = 0
        for i in range(rows):
            for j in range(cols):
                ans = max(ans,dfs(i,j))
        return ans
