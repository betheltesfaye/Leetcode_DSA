# class Solution:
#     def isValid(self, s: str) -> bool:
#         boolVal = False
#         countC = 0
#         countS = 0
#         countR = 0
#         for i in range(0, len(s)-1):
#             if s[i] == "(": 
#                 boolVal = s[(i+1)*-1] == ")" or s[i+1] == ")"
#                 countC += 1
#             if s[i] == "[": 
#                 boolVal = s[(i+1)*-1] == "]" or s[i+1] == "]"
#                 countS += 1
#             if s[i] == "{": 
#                 boolVal = s[(i+1)*-1] == "}" or s[i+1] == "}"
#                 countR += 1
        
#         if (countC + countS + countR)*2 != len(s):
#             print(countC, countS, countR, (countC + countS + countR)*2, len(s))
#             return False
            
#         return boolVal
class Solution:
    def isValid(self, s: str) -> bool:
        # Map closing brackets to their corresponding opening brackets
        bracket_map = {")": "(", "}": "{", "]": "["}
        stack = []
        
        for char in s:
            # If it's a closing bracket
            if char in bracket_map:
                # Pop the top element if stack isn't empty, else use a dummy value
                top_element = stack.pop() if stack else '#'
                
                # If the mapping doesn't match the popped element, it's invalid
                if bracket_map[char] != top_element:
                    return False
            else:
                # It's an opening bracket, push it onto the stack
                stack.append(char)
        
        # If the stack is empty, all brackets found their match
        return len(stack) == 0
            