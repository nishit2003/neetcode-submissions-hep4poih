class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # return sorted(s) == sorted(t)
        S = defaultdict(int)
        T = defaultdict(int)

        for ele in s:
            S[ele] +=1
        for ele in t:
            T[ele] +=1

        if S == T:
            return True
        else:
            return False

        