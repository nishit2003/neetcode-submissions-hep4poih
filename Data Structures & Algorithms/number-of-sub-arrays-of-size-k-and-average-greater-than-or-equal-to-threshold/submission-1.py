class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        target = k * threshold
        curr_sum = sum(arr[:k])
        cnt = 1 if curr_sum >= target else 0

        for i in range(k, len(arr)):
            curr_sum += arr[i]  - arr[i-k]
            if curr_sum >= target:
                cnt +=1

        return cnt