class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        buying = selling = prices[0]
        for price in prices:
            if price < buying:
                buying = price
                selling = price 
            else:
                selling = price 
                max_profit = max(max_profit, selling - buying )

        return max_profit 