class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        directions = [[-1,0],[1,0],[0,1],[0,-1]]
        visit = set()

        def dfs(r,c,i):
            if i == len(word):
                return True
            if r < 0 or c < 0 or r>= rows or c>=cols or board[r][c] != word[i] or (r,c) in visit:
                return False

            visit.add((r,c))
            for dr,dc in directions:
                if dfs(r+dr,c+dc,i+1):
                    return True
            visit.remove((r,c))

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0]:
                    if dfs(r,c,0):
                        return True
        return False

            
