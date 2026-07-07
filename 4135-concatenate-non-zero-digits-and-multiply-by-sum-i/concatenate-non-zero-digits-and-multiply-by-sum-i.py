# class Solution:
#     def sumAndMultiply(self, n: int) -> int:
#         x = ""
#         sum = 0
#         for i in str(n):
#             if int(i) != 0:
#                 x += i
#                 sum += int(i)
                
        
#         final = int(x) * sum

#         return final

class Solution:
    def sumAndMultiply(self, n: int) -> int:
        x = ""
        total_sum = 0
        
        for i in str(n):
            if int(i) != 0:
                x += i
                total_sum += int(i)
        
        # If x is still empty, it means n was 0 or contained only zeros.
        # Otherwise, proceed with the calculation.
        x_val = int(x) if x != "" else 0
        
        return x_val * total_sum