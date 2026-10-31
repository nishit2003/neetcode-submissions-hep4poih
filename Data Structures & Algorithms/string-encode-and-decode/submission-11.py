class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for word in strs:
            size = len(word)
            res += str(size) + "#" + word
        return res

    def decode(self, s: str) -> List[str]:
        i = 0
        res = []
        while i < len(s):
            j = i
            while s[j] != "#":
                j+=1
            num = int(s[i:j])
            word = s[j+1:j+num+1]
            res.append(word)
            i = j + num + 1
        return res
            
