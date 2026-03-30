class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        nums = []
        arr = list(range(1,n+1))
        print(arr)

        def backtrack(i):
            if len(nums) == k:
                res.append(nums.copy())
                return
            if i >= n:
                return
                
            # to choose
            nums.append(arr[i])
            backtrack(i+1)
            nums.pop()

            # to not choose
            backtrack(i+1)

        backtrack(0)
        return res