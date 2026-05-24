class Solution:
    def addBinary(self, a: str, b: str) -> str:
        count1 = 0
        count2 = 0
        totalDecA = 0
        totalDecB = 0
        finalBi = ""
        for char in a[::-1]:
            decA = (int(char) * (2 ** count1))
            count1 += 1
            if int(char) == 1:
                totalDecA += decA
        for char in b[::-1]:
            decB = (int(char) * (2 ** count2))
            count2 += 1
            if int(char) == 1:
                totalDecB += decB
        total = totalDecA + totalDecB
        print(totalDecA)
        print(totalDecB)
        print(total)

        finalBi += str(total % 2)

        while (total // 2) != 0:
            total //= 2
            finalBi += str(total % 2)    

        return finalBi[::-1]
        

        

