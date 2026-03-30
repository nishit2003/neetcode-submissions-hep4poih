class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])

        l, r = 0, rows-1
        while l <= r:
            m = (l + r)//2
            if matrix[m][0] == target:
                return True
            elif matrix[m][0] > target:
                r = m - 1
            elif matrix[m][-1] < target:
                l = m + 1
            else:
                row = m
                break
        else:
            return False  # no valid row found

        l,r = 0,cols - 1
        while l<=r:
            m = (l+r)//2
            if matrix[row][m] > target:
                r = m - 1
            elif matrix[row][m] < target:
                l = m + 1
            else:
                return True
        return False

            