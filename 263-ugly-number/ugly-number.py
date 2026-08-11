class Solution:
    def isUgly(self, n: int) -> bool:
        # A non-positive integer cannot be ugly
        if n <= 0:
            return False
        
        # Repeatedly divide n by 2, 3, and 5
        for factor in [2, 3, 5]:
            while n % factor == 0:
                n //= factor
                
        # If the remaining number is 1, it's an ugly number
        return n == 1

        #Do it again Bethel