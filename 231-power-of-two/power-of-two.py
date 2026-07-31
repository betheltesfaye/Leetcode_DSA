class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # if 2 ** ((int(sqrt(n))) - (sqrt(n))) == n:
        #     return True
        newN = n
        
        if n == 1 or n == 2:
            return True
        if n <= 0:
            return False

        while newN > 2:
            if newN % 2 != 0:
                return False
            else:
                print(newN)
                newN /= 2
                print(newN)
        
        return True
    
        # round(n, 3)) 
       
        # print(f"Int Sqrt:", int(sqrt(n)), 
        # f"Float Sqrt:", round(n, 3))
        # print((int(sqrt(n))) - (sqrt(n)))
        # return False