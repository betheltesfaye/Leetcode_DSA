class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        allInOneStr = ""
        finalList = []
        for i in digits:
            allInOneStr += str(i)

        plus = int(allInOneStr) + 1
        plus = str(plus)
        print(plus)
    
        for j in plus:
            finalList += [int(j)]
        print(finalList)
        return finalList