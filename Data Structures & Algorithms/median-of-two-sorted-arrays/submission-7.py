class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a,b = nums1, nums2
        if len(a) > len(b):
            a,b = b,a
        
        sa = len(a)
        sb = len(b)
        total = sa+sb
        half = total // 2

        l,r = 0, sa-1
        while True:
            m1 = (l+r)//2
            m2 = half - m1 -2

            aleft = a[m1] if m1 >=0 else -float('inf')
            aright = a[m1+1] if m1+1 < sa else float('inf')
            
            bleft = b[m2] if m2 >= 0 else -float('inf')
            bright = b[m2+1] if m2+1 < sb else float('inf')

            if aleft<=bright and bleft <= aright:
                if total %2:
                    return min(aright,bright)
                else:
                    return (max(aleft,bleft)+min(aright,bright))/2
            elif aleft > bright:
                r = m1 - 1
            else:
                l = m1 + 1