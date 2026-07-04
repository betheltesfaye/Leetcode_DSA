class Solution:
    def isUgly(self, n: int) -> bool:
        # Edge case: non-positive integers are not ugly numbers
        if n <= 0:
            return False
        
        # Continuously divide by 2, 3, and 5 as long as it's possible
        for factor in [2, 3, 5]:
            while n % factor == 0:
                n //= factor
        
        # If the remaining number is 1, it means it only had 2, 3, and 5 as prime factors
        return n == 1

        # do it again Bethel