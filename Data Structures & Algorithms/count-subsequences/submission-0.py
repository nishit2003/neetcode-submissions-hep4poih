class Solution:
    def numDistinct(self, s: str, t: str) -> int:

        arr = []
        curr = []
        def backtrack(i):
            if len(curr) == len(t):
                arr.append("".join(curr.copy()))
                return
            if i >= len(s):
                return
            # to include
            curr.append(s[i])
            backtrack(i+1)
            curr.pop()

            # to exclude
            backtrack(i+1)

        backtrack(0)

        memo = {}
        def helper(s1,t1,i,j):
            if i == len(s1) and j == len(t1):
                return True
            if i > len(s1) or j > len(t1):
                return False
            if (s1,t1,i,j) in memo:
                return memo[(s1,t1,i,j)]
            if s1[i] == t1[j]:
                memo[(s1,t1,i,j)] = helper(s1,t1,i+1,j+1)
            else:
                memo[(s1,t1,i,j)] = helper(s1,t1,i+1,j) or helper(s1,t1,i,j+1)
            return memo[(s1,t1,i,j)]

        res = 0
        for i in range(len(arr)):
            # if helper(arr[i],t,0,0):
            #     res +=1
            if arr[i] == t:
                res += 1
        return res