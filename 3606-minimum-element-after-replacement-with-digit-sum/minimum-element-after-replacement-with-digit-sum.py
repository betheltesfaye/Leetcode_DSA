class Solution:
    def minElement(self, nums: List[int]) -> int:
        sumDigits = 0
        finalList = []
        for i in nums:
            for j in str(i):
                sumDigits += int(j)
            finalList.append(sumDigits)
            sumDigits = 0

        return min(finalList) 