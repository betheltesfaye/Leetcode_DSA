class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        # digits = []
        # digitTen = n
        # productOfDigits = 1 
        # sumOfDigits = 0
        # count = 0
        # if n < 10:
        #     return 0
        
        # while digitTen > 0:
        #     digitTen //= 10
        #     count += 1
        
        # for i in range(1, count+1):
        #     digitTen = n - ((n//10**i) * (10**i))
        #     if digitTen < 10:
        #         digits.append(digitTen)
        #     else:
        #         digits.append(digitTen // (10**(i-1)))
    
        # print(digits)
        digits = []
        productOfDigits = 1 
        sumOfDigits = 0

        if n < 10:
            return 0

        # Extract digits directly using modulo
        while n > 0:
            digits.append(n % 10)  # Captures the last digit (even if it is 0)
            n //= 10              # Shrinks the number down

            # For 705, digits will be [5, 0, 7]
            # If you need them in original order [7, 0, 5], just reverse it:
        
        for i in digits:
            productOfDigits *= i
            sumOfDigits += i 
        
        print(digits)
        return productOfDigits - sumOfDigits
        
        
        
        
        
        