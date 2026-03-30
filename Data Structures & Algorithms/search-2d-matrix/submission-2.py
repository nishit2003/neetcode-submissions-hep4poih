class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows , cols = len(matrix), len(matrix[0]) 
        top, btm = 0 , rows -1 

        while top <= btm:
            m = (top + btm) // 2
            if matrix[m][-1] < target:
                top = m + 1
            elif matrix[m][0] > target:
                btm = m - 1
            else:
                break

        row = (top + btm) // 2
        l , r = 0 , cols - 1
        while l <=r:
            m = l+((r-l)//2)
            if target > matrix[row][m]:
                l = m +1
            elif target < matrix[row][m]:
                r = m - 1
            else:
                return True
        return False

          