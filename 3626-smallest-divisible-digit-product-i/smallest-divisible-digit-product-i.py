class Solution:
    def smallestNumber(self, n: int, t: int) -> int:       
        for i in range(n*t):
            x = 1
            for i in str(n):
                x *= int(i)
            if x % t == 0:
                return n
            else:
                n += 1