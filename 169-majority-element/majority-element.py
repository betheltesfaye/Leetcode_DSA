# class Solution:
#     def majorityElement(self, nums: List[int]) -> int:
#         nums.sort()
#         for i in nums:
#             if nums.count(i) >= len(nums) / 2:
#                 return i
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums) // 2]
