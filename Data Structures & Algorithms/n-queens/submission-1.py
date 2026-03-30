class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        colset = set()
        posdiag = set()
        negdiag = set()

        res = []
        board = [["."] * n for i in range(n)]

        def backtrack(r):
            if r == n:
                res.append(["".join(row) for row in board])
                return
            
            for c in range(n):
                if c in colset or (r+c) in posdiag or (r-c) in negdiag:
                    continue
                
                colset.add(c)
                posdiag.add(r+c)
                negdiag.add(r-c)
                board[r][c] = "Q"

                backtrack(r+1)

                colset.remove(c)
                posdiag.remove(r+c)
                negdiag.remove(r-c)
                board[r][c] = "."
        backtrack(0)
        return res

