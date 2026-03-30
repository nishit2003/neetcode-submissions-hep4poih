class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)

        if n1 > n2:
            return False

        #[1,1,1,0,0,0,,0,]
        s1_arr = [0] * 26
        s2_arr = [0] * 26

        for i in range(n1):
            s1_arr[ord(s1[i])-ord('a')] +=1 
            s2_arr[ord(s2[i])-ord('a')] +=1 

        if s1_arr == s2_arr:
            return True

        for i in range(n1, n2):
            s2_arr[ord(s2[i])-ord('a')] +=1
            s2_arr[ord(s2[i-n1])-ord('a')] -=1
            if s1_arr == s2_arr:
                return True
        
        return False


