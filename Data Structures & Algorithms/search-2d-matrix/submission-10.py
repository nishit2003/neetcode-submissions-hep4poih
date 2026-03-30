class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows ,cols = len(matrix) , len(matrix[0])

        top, btm = 0 , rows - 1
        while top <= btm:
            row =  top + ((btm-top) // 2)
            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                btm = row - 1
            else:
                break

        if not (top<= btm):
            return False

        l , r = 0 , cols - 1
        row = top + ((btm - top) // 2)
        while l<=r:
            m = l + ((r-l)//2)
            if target > matrix[row][m]:
                l = m + 1
            elif target < matrix[row][m]:
                r = m - 1 
            else:
                return True
        return False

