class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for word in strs:
            size = len(word)
            s+= str(size)+"#"+word

        return s

    def decode(self, s: str) -> List[str]:
        res = []

        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j+=1
            num = int(s[i:j])
            word = s[j+1: j+1+num]
            res.append(word)
            i = j + 1 + num
            
        return res