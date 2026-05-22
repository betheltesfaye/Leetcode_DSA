class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs: return "" # Good to handle empty lists!
        
        longestPrefix = ""
        smallestLen = len(min(strs, key=len))

        # Outer loop: x is the length we are testing
        for x in range(1, smallestLen + 1):
            candidate = strs[0][:x]
    
            # Everything below must be indented to be inside the x loop
            for j in strs:
                if not j.startswith(candidate):
                    return longestPrefix 
            
            # This only runs if NO mismatches were found in the inner loop
            longestPrefix = candidate

        return longestPrefix