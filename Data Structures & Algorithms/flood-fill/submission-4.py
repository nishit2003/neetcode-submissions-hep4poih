class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        rows, cols = len(image), len(image[0])
        directions = [[0,1],[1,0],[-1,0],[0,-1]]
        # visit = set()
        OG = image[sr][sc]

        if color == OG:
            return image

        def dfs(r,c):
            if r < 0 or c < 0 or r>=rows or c >= cols or image[r][c] != OG:
                return

            image[r][c] = color
            for dr,dc in directions:
                dfs(r+dr,c+dc)    
        
        dfs(sr,sc)
        return image