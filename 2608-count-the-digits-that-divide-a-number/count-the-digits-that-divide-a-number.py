# class Solution:
#     def countDigits(self, num: int) -> int:
#         val = 0
#         for i in range (1, num + 1):
#             if num % i == 0:
#                 val += 1
        
#         return val
class Solution:
    def countDigits(self, num: int) -> int:
        count = 0
        temp = num
        
        while temp > 0:
            # Get the last digit
            digit = temp % 10
            
            # Check if it divides the original num
            if num % digit == 0:
                count += 1
            
            # Remove the last digit
            temp //= 10
            
        return count