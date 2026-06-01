# class Solution:
#     def countKeyChanges(self, s: str) -> int:
#         s = s.lower()
#         changes = 0
        
#         # Start from the second character (index 1)
#         for i in range(1, len(s)):
#             # If current char is different from previous, it's a key change
#             if s[i] != s[i-1]:
#                 changes += 1
                
#         return changes

class Solution:
    def countKeyChanges(self, s: str) -> int:
        s = s.lower()
        changes = 0
        
        # Start from the second character (index 1)
        for i in range(len(s) - 1):
            # If current char is different from previous, it's a key change
            if s[i] != s[i+1]:
                changes += 1
                
        return changes
        
