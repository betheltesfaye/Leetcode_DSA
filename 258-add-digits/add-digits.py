class Solution:
    def addDigits(self, num: int) -> int:
        
        while len(str(num)) > 1:
            
            addDigits = 0
            for i in range(len(str(num))):
                addDigits += int(str(num)[i])
        
            num = addDigits
        
        return num

        