class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        
        cnts1 = {}
        cnts2 = {}

        for i in range(len(s1)):
            cnts1[s1[i]] = 1 + cnts1.get(s1[i],0)
            cnts2[s2[i]] = 1 + cnts2.get(s2[i],0)
        
        if cnts2 == cnts1:
            return True

        l1, l2 = len(s1), len(s2)
        
        l=0
        for r in range(l1, l2):
            cnts2[s2[r]] = 1 + cnts2.get(s2[r],0)
            if len(s2) > len(s1):
                cnts2[s2[l]] -= 1
                if cnts2[s2[l]] == 0:
                    del cnts2[s2[l]]
                l+=1
            if cnts2 == cnts1:
                return True

            
        return False