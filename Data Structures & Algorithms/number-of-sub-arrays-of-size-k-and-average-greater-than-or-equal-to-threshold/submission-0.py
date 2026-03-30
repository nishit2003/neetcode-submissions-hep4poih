class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        curr = sum(arr[:k-1])
        res = 0
        for l in range(len(arr)-k+1):
            curr += arr[l+k-1]
            if (curr/k) >= threshold:
                res+=1
            curr-=arr[l]
        return res
