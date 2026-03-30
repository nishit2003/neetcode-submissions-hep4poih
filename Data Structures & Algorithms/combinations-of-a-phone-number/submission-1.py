class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
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

        def backtrack(i,curr):
            if len(curr) == len(digits):
                res.append(curr.lower())
                return
            for c in data[digits[i]]:
                backtrack(i+1, curr + c)

        if digits:
            backtrack(0,"")

        return res
