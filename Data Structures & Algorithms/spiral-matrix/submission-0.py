class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        l, r = 0 , len(matrix[0])
        t, b = 0 , len(matrix)
        res = []
        while l < r and t < b:
            # top row
            for i in range(l,r):
                res.append(matrix[t][i])
            t+=1

            # rightmost col
            for i in range(t,b):
                res.append(matrix[i][r-1])
            r-=1

            # bottom row
            if t < b:
                for i in range(r-1,l-1,-1):
                    res.append(matrix[b-1][i])
                b-=1

            # leftmost row
            if l < r:
                for i in range(b-1,t-1,-1):
                    res.append(matrix[i][l])
                l+=1
        
        return res

