class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        

        res = ''
        if columnNumber <= 26:
            return chr((columnNumber-1) + ord("A"))
        else:
            while columnNumber:
                columnNumber-=1
                # val = columnNumber // 26
                # res += (chr((val) + ord("A")))
                # columnNumber -= val
                remainder = columnNumber % 26
                res += chr((remainder) + ord("A"))
                columnNumber = columnNumber // 26
                
        return res[::-1]
# 52 -> AZ
# val 2 
# colN = 51
# res = "AZ