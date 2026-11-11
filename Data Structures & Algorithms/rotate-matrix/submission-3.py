class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        l,r = 0, len(matrix) - 1

        while l <= r:
            for i in range(r-l):
                top,btm = l,r
                topleft = matrix[top][l+i]

                matrix[top][l+i] = matrix[btm-i][l]

                matrix[btm-i][l] = matrix[btm][r-i]

                matrix[btm][r-i] = matrix[top+i][r]

                matrix[top+i][r] = topleft

            l+=1
            r-=1
