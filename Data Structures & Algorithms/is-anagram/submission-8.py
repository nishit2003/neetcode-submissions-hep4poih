class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        cnts = {}
        cntt = {}

        for i in range(len(s)):
            cnts[s[i]] = 1 + cnts.get(s[i],0)
            cntt[t[i]] = 1 + cntt.get(t[i],0)

        # print(cnts,)
        return cnts == cntt