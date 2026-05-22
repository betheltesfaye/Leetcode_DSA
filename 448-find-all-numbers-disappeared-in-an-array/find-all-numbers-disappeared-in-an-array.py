class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        if max(nums) > len(nums):
            ogArray = list(range(1, max(nums) + 1))
        else:
            ogArray = list(range(1, len(nums) + 1))
            
        disNums = list(set(ogArray) ^ set(nums))

        return disNums
    