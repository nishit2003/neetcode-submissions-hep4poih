class SparseVector:
    def __init__(self, nums: List[int]):
        self.vector=nums
        self.nonZero=set()
        for i,n in enumerate(nums):
            if n: self.nonZero.add(i)

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        res=0
        for idx in self.nonZero:
            if idx in vec.nonZero:
                res+=self.vector[idx]*vec.vector[idx]
        return res

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)
