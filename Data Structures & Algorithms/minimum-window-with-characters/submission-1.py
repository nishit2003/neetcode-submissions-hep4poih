class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l = 0
        if t == "" or len(t) > len(s):
            return ""
        countT, window = {}, {}
        for c in t:
            countT[c] = 1 + countT.get(c,0)
        have,need = 0,len(countT)
        res, minres = [-1,-1], float("inf")
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c,0)

            if c in countT and countT[c] == window[c]:
                have +=1

            while have == need:
                if (r-l+1) < minres:
                    res = [l,r]
                    minres = r-l+1
                
                window[s[l]]-=1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have-=1
                l+=1

        l,r = res
        return s[l:r+1] if minres != float('inf') else ""
        


        