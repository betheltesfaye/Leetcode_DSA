# class Solution:
#     def detectCapitalUse(self, word: str) -> bool:
#         # 1. All letters are capitals (e.g., "USA")
#         # 2. All letters are not capitals (e.g., "leetcode")
#         # 3. Only the first letter is capital (e.g., "Google")
        
#         return word.isupper() or word.islower() or word.istitle()

class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        capital_count = 0
        
        # Count total uppercase letters
        for char in word:
            if char.isupper():
                capital_count += 1
                
        # Rule 1: All capitals
        if capital_count == len(word):
            return True
            
        # Rule 2: All lowercase
        if capital_count == 0:
            return True
            
        # Rule 3: Only the first letter is capital
        if capital_count == 1 and word[0].isupper():
            return True
            
        # If it doesn't match any rule
        return False