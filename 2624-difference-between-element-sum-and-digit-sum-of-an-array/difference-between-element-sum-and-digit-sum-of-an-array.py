class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        total = []
        digitTotal = []
        for i in nums:
            if len(str(i)) <= 1:
                digitTotal += [i]
            else:
                for j in str(i):
                    digitTotal += [int(j)]
        
        return sum(nums) - sum(digitTotal)