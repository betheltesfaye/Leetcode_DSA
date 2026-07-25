class Solution:
    def isMiddleElementUnique(self, nums: list[int]) -> bool:
        midNum = int((len(nums) - 1) / 2)

        print(midNum)
        print(nums[midNum])
        if nums.count(nums[midNum]) == 1:
            return True
        else:
            return False