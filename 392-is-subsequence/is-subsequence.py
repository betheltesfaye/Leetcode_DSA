class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_idx = 0
        t_idx = 0
        
        # Scan through both strings
        while s_idx < len(s) and t_idx < len(t):
            # If the characters match, move to the next character in s
            if s[s_idx] == t[t_idx]:
                s_idx += 1
            # Always move forward in t
            t_idx += 1
            
        # If we matched every character in s, s_idx will reach the end
        return s_idx == len(s)

#Do again!
                