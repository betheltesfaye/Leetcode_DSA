class Solution:
    def mySqrt(self, x: int) -> int:
        # Base cases: the square root of 0 is 0, and 1 is 1
        if x < 2:
            return x
            
        # The square root of x (for x >= 2) will always be between 2 and x // 2
        low = 2
        high = x // 2
        ans = 1 # Tracks the closest integer floor found so far
        
        while low <= high:
            mid = (low + high) // 2
            square = mid * mid
            
            if square == x:
                return mid
            elif square < x:
                ans = mid      # mid could be the potential answer, save it
                low = mid + 1  # Search the right half for a closer answer
            else:
                high = mid - 1 # Search the left half
                
        return ans 

# need to redo this exersise