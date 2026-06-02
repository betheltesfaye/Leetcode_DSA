# class Solution:
#     def triangleType(self, nums: List[int]) -> str:
#         a = nums[0]
#         b = nums[1]
#         c = nums[2]

#         if a == b and b == c:
#             return "equilateral"
#         if a != b and a != c and b != c:
#             return "scalene"
#         else:
#             return "isosceles" 

class Solution:
    def triangleType(self, nums: List[int]) -> str:
        a, b, c = nums
        
        # 1. Check if it is a valid triangle first
        # Sort the sides: side1 <= side2 <= side3
        s = sorted(nums)
        if s[0] + s[1] <= s[2]:
            return "none"
            
        # 2. Determine the type
        if a == b == c:
            return "equilateral"
        if a == b or a == c or b == c:
            return "isosceles"
        return "scalene"