class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        res = 0
        data = defaultdict(int)
        for r in range(len(s)):
            data[s[r]]+=1
            if (r-l+1) - max(data.values()) > k:
                data[s[l]]-=1
                l+=1
            res = max(res, r-l+1)
        return res
