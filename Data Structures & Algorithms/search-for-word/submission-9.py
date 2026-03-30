class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        directions = [[0,1],[1,0],[-1,0],[0,-1]]
        seen = set()

        def dfs(r,c,i):
            if i == len(word):
                return True
            if (r<0 or c<0 or
            r >= rows or c >= cols or
            board[r][c] != word[i]
            or (r,c) in seen):
                return False
        
            seen.add((r,c))
            for dr,dc in directions:
                if dfs(dr+r,c+dc,i+1):
                    return True
            seen.remove((r,c))

        for i in range(rows):
            for j in range(cols):
                if dfs(i,j,0): return True
        return False