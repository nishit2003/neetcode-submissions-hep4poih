class Solution:
    def maxSumDistinctTriplet(self, x: List[int], y: List[int]) -> int:
        freq = {}
        for ch in x:
            freq[ch] = 1 + freq.get(ch,0)
        
        if len(freq) < 3:
            return -1

        maxval = {}
        for i in range(len(x)):
            if x[i] not in maxval:
                maxval[x[i]] = y[i]
            maxval[x[i]] = max(maxval[x[i]],y[i])

        values = maxval.values()
        return sum(sorted(values)[-3:])