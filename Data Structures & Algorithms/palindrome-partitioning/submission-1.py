class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        subset = []

        def dfs(start):
            if start >= len(s):
                res.append(subset.copy())
                return

            for end in range(start,len(s)):
                if self.Pal(s,start,end):
                    subset.append(s[start:end+1])
                    dfs(end+1)
                    subset.pop()

        dfs(0)
        return res

    def Pal(self,s,l,r):
        while l < r:
            if s[l] != s[r]:
                return False
            l, r = l + 1, r - 1
        return True

            