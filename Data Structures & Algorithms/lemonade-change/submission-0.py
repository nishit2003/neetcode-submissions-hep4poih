class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        
        five, tens = 0,0
        for b in bills:
            if b == 5:
                five +=1
            elif b == 10:
                tens +=1
                if five > 0:
                    five -= 1
                else:
                    return False
                
            else:
                if five > 0 and tens > 0:
                    five -= 1
                    tens -= 1
                elif five >= 3:
                    five -= 3
                else:
                    return False
        return True
        