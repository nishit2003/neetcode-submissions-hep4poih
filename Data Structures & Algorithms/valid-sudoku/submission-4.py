class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = defaultdict(set)
        col = defaultdict(set)
        box = defaultdict(set)

        rows, cols = len(board), len(board[0])
        # num = board[r][c]

        for r in range(rows):
            for c in range(cols):
                num = board[r][c]
                if board[r][c] == ".":
                    continue
                elif (num in row[r] or
                    num in col[c] or
                    num in box[r//3,c//3]):
                    return False
                else:
                    row[r].add(num)
                    col[c].add(num)
                    box[(r//3,c//3)].add(num)
                

        return True
             
