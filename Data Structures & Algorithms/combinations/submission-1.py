class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        curr, res = [],[]

        arr = [i for i in range(1,n+1)]
        print(arr)

        def dfs(i):
            if len(curr) == k:
                res.append(curr.copy())
                return
            if i >= len(arr):
                return
            # to include 
            curr.append(arr[i])
            dfs(i+1)

            # to not include
            curr.pop()
            dfs(i+1)

        dfs(0)
        return res


