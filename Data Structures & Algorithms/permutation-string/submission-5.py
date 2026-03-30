class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        S1 = [0] * 26
        S2 = [0] * 26

        for i in range(len(s1)):
            S1[ord(s1[i]) - ord("s")] +=1
            S2[ord(s2[i]) - ord("s")] +=1
        
        if S1 == S2:
            return True

        for i in range(len(s1),len(s2)):
            S2[ord(s2[i]) - ord("s")] +=1
            S2[ord(s2[i-len(s1)]) - ord("s")] -=1
            if S1 == S2:
                return True

        return False