class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        data = {
            "2":"abc", "3":"def", "4":"ghi", "5" : "jkl", "6" : "mno" , "7" : "pqrs" , "8":"tuv" , "9": "wxyz"
        }

        if not digits:
            return []

        res = []
        curr = []
        def backtrack(i):
            if i == len(digits):
                res.append("".join(curr.copy()))
                return
            
            if i >= len(digits):
                return

            for ch in data[digits[i]]:
                curr.append(ch)
                backtrack(i+1)

                curr.pop()
        
        backtrack(0)
        return res