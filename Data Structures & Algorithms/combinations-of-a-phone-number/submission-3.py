class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
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

        res = []
        nums = []

        def backtrack(i):
            if len(nums) == len(digits):
                res.append("".join(nums.copy()))
                return

            if i >= len(digits):
                return

            # to choose
            for ch in data[digits[i]]:
                nums.append(ch.lower())
                backtrack(i+1)
                nums.pop()

        backtrack(0)
        return res