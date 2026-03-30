class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        if target < matrix[0][0] or target > matrix[-1][-1]:
            return False

        top, btm = 0, rows - 1
        while top <= btm:
            mid = (top + btm) // 2
            if target > matrix[mid][-1]:
                top = mid + 1
            elif target < matrix[mid][0]:
                btm = mid - 1
            else:
                break

        l , r = 0 , cols - 1
        while l <= r:
            m = (l + r) // 2
            if target > matrix[mid][m]:
                l = m + 1
            elif target < matrix[mid][m]:
                r = m - 1
            else:
                return True
        return False

