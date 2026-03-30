class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        curr = []
        res = []
        data = {
            '2':"ABC",
            '3':"DEF",
            '4':"GHI",
            '5':"JKL",
            '6':"MNO",
            '7':"PQRS",
            '8':"TUV",
            '9':"WXYZ"
        }
        def backtrack(i):
            if i == len(digits):
                res.append("".join(curr))
            if i >= len(digits):
                return
            for ch in data[digits[i]]:
                curr.append(ch.lower())
                backtrack(i+1)
                curr.pop()
        backtrack(0)
        return res
