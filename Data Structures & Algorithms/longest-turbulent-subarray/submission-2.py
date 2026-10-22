class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        flag = None
        res = 0
        n = len(arr)
        curr =0
        for i in range(n-1):
            if arr[i] > arr[i+1]:
                curr = curr+ 1 if flag is True else 1
                flag = False
            elif arr[i] < arr[i+1]:
                curr = curr + 1 if flag is False else 1
                flag = True
            else:
                curr = 0
                flag = None
            res = max(res,curr)
        
        return res +1
