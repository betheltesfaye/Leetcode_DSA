class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        sumOfSingle = 0
        sumOfDouble = 0
        for i in nums:
            if i >= 10:
                sumOfDouble += i
            elif i <= 9:
                sumOfSingle += i
        
        if sumOfDouble == sumOfSingle:
            return False
        else:
            return True