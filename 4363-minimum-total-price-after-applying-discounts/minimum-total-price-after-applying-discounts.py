class Solution:
    def minPrice(self, prices: list[int], discounts: list[int]) -> float:
        
        prices.sort(reverse=True)
        discounts.sort(reverse=True)
        
        chosenLen = 0
        outputList = []

        if len(discounts) < len(prices):
            chosenLen = len(discounts)
        else:
            chosenLen = len(prices)


        for i in range(chosenLen):
            outputList.append((prices[i] * (100 - discounts[i])) / 100)

        print(outputList)
        print(prices[i+1:])
        
        return sum(outputList) + sum(prices[i+1:])
    