# class Solution:
#     def firstUniqChar(self, s: str) -> int:
#         count = 0
#         MyList = []
#         for i in s:
#             for j in range(i, len(s)):
#                 if i == s[j]:
#                     MyList []
                
class Solution:
    def firstUniqChar(self, s: str) -> int:
        # Dictionary to store the frequency of each character
        count_map = {}
        
        # First pass: count frequencies
        for char in s:
            count_map[char] = count_map.get(char, 0) + 1
            
        # Second pass: find the index of the first character with a count of 1
        for index, char in enumerate(s):
            if count_map[char] == 1:
                return index
                
        return -1                    

            
