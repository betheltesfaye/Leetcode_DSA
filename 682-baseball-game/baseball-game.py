# class Solution:
#     def calPoints(self, operations: List[str]) -> int:
#         record = []
#         for i in operations:
#             if i.isdigit() and int(i):
#                 record.append(int(i))
#             if i == '+':
#                 record.append(sum(record[-2:]))
#                 print(record)
#             if i == 'D':
#                 record.append(record[-1]*2)
#             if i == 'C':
#                 record.pop()
        
#         return sum(record)

class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        
        for i in operations:
            if i == '+':
                record.append(sum(record[-2:]))
            elif i == 'D':
                record.append(record[-1] * 2)
            elif i == 'C':
                record.pop()
            else:
                # If it's not +, D, or C, it MUST be an integer (e.g., "5" or "-5")
                record.append(int(i))
        
        return sum(record)
