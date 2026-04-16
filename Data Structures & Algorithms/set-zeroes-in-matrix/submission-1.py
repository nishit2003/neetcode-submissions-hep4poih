class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        Rows, Cols = len(matrix), len(matrix[0])
        rows, cols = [False] * Rows, [False] * Cols

        for r in range(Rows):
            for c in range(Cols):
                if matrix[r][c] == 0:
                    rows[r] = True
                    cols[c] = True

        for r in range(Rows):
            for c in range(Cols):
                if rows[r] or cols[c]:
                    matrix[r][c] = 0
