class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowset = {i:set() for i in range(9)}
        colset = {i:set() for i in range(9)}
        boxset = {(i, j): set() for i in range(3) for j in range(3)}

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if board[r][c] in rowset[r] or board[r][c] in colset[c] or board[r][c] in boxset[(r // 3, c // 3)]:
                    return False
                colset[c].add(board[r][c])
                rowset[r].add(board[r][c])
                boxset[(r // 3, c // 3)].add(board[r][c])
        return True

