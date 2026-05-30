class Solution:
    def sumOfMultiples(self, n: int) -> int:
        count = 1
        sumOfMult = 0
        while count <= n:
            if count%3 == 0 or count%5 == 0 or count%7 == 0:
                sumOfMult += count
                count += 1
            else:
                count += 1
             
        return sumOfMult