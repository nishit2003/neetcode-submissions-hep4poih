class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = set()
        posdiag = set()
        negdiag = set()

        res = []
        board = [["."] * n for i in range(n)]
        
        def dfs(r):
            if r == n:
                res.append(["".join(row) for row in board])
                return

            for c in range(n):
                if c in col or (r+c) in posdiag or (r-c) in negdiag:
                    continue

                col.add(c)
                posdiag.add(r+c)
                negdiag.add(r-c)
                board[r][c] = "Q"

                dfs(r+1)

                col.remove(c)
                posdiag.remove(r+c)
                negdiag.remove(r-c)
                board[r][c] = "."
        dfs(0)
        return res    