# class Solution:
#     def missingNumber(self, nums: List[int]) -> int:
#         nums.sort()
#         totalSum = len(nums) * (len(nums) + 1) // 2
#         initialSum = 0
#         perfectNums = []
#         # for i in nums:
#         #     initialSum += i

#         for i in range(len(nums)):
#             perfectNums.append(i)

#         missingNum = int(set(perfectNums) - set(nums))
   

#         return missingNum

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # 1. Get the expected sum using the O(1) formula
        totalSum = len(nums) * (len(nums) + 1) // 2
        
        # 2. Get the actual sum using Python's built-in sum()
        actualSum = sum(nums)
        
        # 3. The difference is your missing number
        return totalSum - actualSum
