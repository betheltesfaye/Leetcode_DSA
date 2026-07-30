class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        answer = ""
        final = []
        for i in range(1, n+1):
            if (i % 3 == 0) and (i % 5 == 0):
                final.append("FizzBuzz")
                continue
            if (i % 3 == 0):
                final.append("Fizz")
                continue
            if (i % 5 == 0):
                final.append("Buzz")
                continue
            
            final.append(str(i))
       
        return final


        
        