class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        q = deque()
        l,r = 0,0

        while r < len(nums):
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)


            left = r - k + 1
            if q[0] < left:
                q.popleft()
            
            if r >= k - 1:
                res.append(nums[q[0]])
            r+=1
        return res