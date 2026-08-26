class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buying_price = prices[0]
        max_profit = 0 
        for price in prices:
            if price > buying_price:
                profit = price - buying_price 
                if profit > max_profit:
                    max_profit = profit 
            else:
                buying_price = price 

        return max_profit 