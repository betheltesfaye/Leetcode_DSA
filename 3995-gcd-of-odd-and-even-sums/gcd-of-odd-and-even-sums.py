class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        sumOdd = []
        sumEven = []
        gcd = 0
        count = 0

        while len(sumOdd) < n:
            count += 1
            if count % 2 != 0:
                sumOdd.append(count)
            else:
                sumEven.append(count)
            
        return math.gcd(sum(sumOdd), sum(sumEven))
        #I literally couldn't understand the question