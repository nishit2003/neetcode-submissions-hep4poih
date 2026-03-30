class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        mapp = defaultdict(int)
        res = 0
        for r in range(len(s)):
            mapp[s[r]] += 1
            while (r-l+1) - max(mapp.values()) > k:
                mapp[s[l]] -= 1
                l+=1

            
            res = max(res, r - l + 1)
        return res



