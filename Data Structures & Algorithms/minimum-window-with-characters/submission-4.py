class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        have = 0
        cntT = {}
        for ele in t:
            cntT[ele] = 1+ cntT.get(ele,0)
        need = len(cntT)
        res = ""
        reslen = float('inf')
        l = 0
        cntS = {}
        for r in range(len(s)):
            ch = s[r]
            cntS[ch] = 1 + cntS.get(ch,0)
            if ch in cntT and cntT[ch] == cntS[ch]:
                have +=1

            while have == need:
                if reslen > (r-l+1):
                    res = s[l:r+1]
                    reslen = r-l+1
                cntS[s[l]]-=1
                if s[l] in cntT and cntS[s[l]] < cntT[s[l]]:
                    have -=1
                l+=1
        # l,r = res
        return res if reslen != float('inf') else ""