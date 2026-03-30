class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        
        cnt1,cnt2 = {},{}
        for i in range(len(s1)):
            cnt1[s1[i]] = 1 + cnt1.get(s1[i],0)
            cnt2[s2[i]] = 1 + cnt2.get(s2[i],0)
        print(cnt1,cnt2)
        if cnt1 == cnt2:
            return True

        for i in range(len(s1),len(s2)):
            cnt2[s2[i]] = 1 + cnt2.get(s2[i],0)
            cnt2[s2[i-len(s1)]] =  cnt2.get(s2[i-len(s1)],0) - 1
            if cnt2[s2[i-len(s1)]] == 0:
                del cnt2[s2[i-len(s1)]]
            if cnt1 == cnt2:
                return True
            print(cnt2)
        return False