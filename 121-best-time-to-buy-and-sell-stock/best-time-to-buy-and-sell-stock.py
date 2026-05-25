# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         §buy = min(prices)
#         buyPosition = prices.index(buy)
#         sell = max(prices[buyPosition:])
#         profit = sell - buy

#         return profit

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Initialize with infinity so any first price will be lower
        min_price = float('inf')
        max_profit = 0
        
        for price in prices:
            # 1. Update the lowest price encountered so far
            if price < min_price:
                min_price = price
            
            # 2. Calculate potential profit if we sold today
            # If current price - min_price is better than max_profit, update it
            elif price - min_price > max_profit:
                max_profit = price - min_price
                
        return max_profit
