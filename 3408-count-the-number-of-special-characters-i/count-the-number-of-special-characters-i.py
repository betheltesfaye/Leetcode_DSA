# class Solution:
#     def numberOfSpecialChars(self, word: str) -> int:
#         upC = []
#         loC = []
#         compareC = []
#         compareC1 = []
#         compareC2 = []
#         count = 0
#         for char in word: 
#             if char.isupper():
#                 upC.append(char)
#             else:
#                 loC.append(char)
        
#         for char in loC:
#             count

class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        # Use sets to store unique characters for O(1) lookup
        lower_chars = set()
        upper_chars = set()
        
        for char in word:
            if char.islower():
                lower_chars.add(char)
            else:
                upper_chars.add(char)
        
        # Count how many characters exist in both sets
        count = 0
        # Iterate through the alphabet to check each letter
        for char_code in range(ord('a'), ord('z') + 1):
            char = chr(char_code)
            if char in lower_chars and char.upper() in upper_chars:
                count += 1
                
        return count
