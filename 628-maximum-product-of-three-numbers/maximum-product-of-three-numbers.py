# class Solution:
#     def maximumProduct(self, nums: List[int]) -> int:
#         nums.sort()
#         absoluteList = []
#         absoluteList2 = []
#         prod = 1
#         count = 0
#         for i in nums:
#             absoluteList.append(abs(i))
#             absoluteList2.append(abs(i))
        
#         absoluteList2.sort(reverse=True)
#         # print(nums)
#         # print(absoluteList)
#         print(absoluteList2)
        
#         for i in absoluteList2:
#             prod *= i
#             count += 1
#             if (count == 3) and (prod > 0):
#                 return prod
#             elif (count == 3) and (prod < 0):
#                 prod /= i
#             #     print(prod)

#         # print(prod)
#         # print(absoluteList.index(1))

from typing import List

class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        
        # Scenario 1: Product of the 3 largest elements
        prod1 = nums[-1] * nums[-2] * nums[-3]
        
        # Scenario 2: Product of 2 smallest (most negative) and the largest element
        prod2 = nums[0] * nums[1] * nums[-1]
        
        return max(prod1, prod2)          