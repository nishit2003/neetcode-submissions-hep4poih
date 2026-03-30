class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False


        S = defaultdict(int)
        T = defaultdict(int)

        for i in s:
            S[i] += 1
            
        for i in t:
            T[i] += 1

        for values in S:
            if S[values] != T[values]:
                return False
            
        return True