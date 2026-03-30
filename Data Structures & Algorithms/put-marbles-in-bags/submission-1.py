class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        splits = []
        if k==1:
            return 0

        for i in range(len(weights)-1):
            splits.append(weights[i]+weights[i+1]) 
        
        splits.sort()
        
        maxsub = weights[0]+ weights[-1] + sum(splits[-(k-1):])
        minsub = weights[0]+ weights[-1] + sum(splits[:k-1])

        return maxsub - minsub