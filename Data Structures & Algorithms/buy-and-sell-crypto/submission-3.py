class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buying_price = prices[0]
        for price in prices:
            if price < buying_price:
                buying_price = price 
            else:
                profit = max(profit, price - buying_price)

        return profit 