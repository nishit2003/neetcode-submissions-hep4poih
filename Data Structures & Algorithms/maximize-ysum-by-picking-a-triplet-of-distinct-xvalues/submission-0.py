class Solution:
    def maxSumDistinctTriplet(self, x: List[int], y: List[int]) -> int:
        freqx = collections.Counter(x)
        if len(freqx.items()) < 3:
            return -1
        mp = {}
        for i in range(len(x)):
            if x[i] not in mp:
                mp[x[i]] = y[i]

            mp[x[i]] = max(mp[x[i]],y[i])
        
        return sum(sorted(list(mp.values()))[-3:])

