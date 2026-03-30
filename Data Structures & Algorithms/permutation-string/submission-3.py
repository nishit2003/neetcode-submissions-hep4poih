class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False
        n1 = len(s1)
        n2 = len(s2)
        s1A = [0]*26
        s2A = [0]*26

        for i in range(n1): 
            s1A[ord(s1[i])-ord("a")] +=1
            s2A[ord(s2[i])-ord("a")] +=1

        if s1A == s2A:
            return True

        for i in range(n1,n2):
            s2A[ord(s2[i])-ord("a")] +=1
            s2A[ord(s2[i-n1])-ord("a")] -=1
            if s1A == s2A:
                return True

        return False
