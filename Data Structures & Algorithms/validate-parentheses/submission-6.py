class Solution:
    def isValid(self, s: str) -> bool:
        valid = {"}":"{","]":"[",")":"("}
        arr = []
        for i in s:
            if i not in valid:
                arr.append(i)
            else:
                if arr and arr[-1] == valid[i]:
                    arr.pop()
                
                else:
                    return False
                
            
        return not arr