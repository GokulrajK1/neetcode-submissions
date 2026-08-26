class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        n = len(prices)
        
        def backtrack(i, can_buy, memo):

            if (i, can_buy) in memo:
                return memo[(i, can_buy)]
            
            if i >= n:
                return 0 
            
            buying = selling = 0
            if can_buy:
                buying = -prices[i] + backtrack(i + 1, False, memo)
            else:
                selling = prices[i] + backtrack(i + 2, True, memo)

            memo[(i, can_buy)] = max(buying, selling, backtrack(i + 1, can_buy, memo))
            return memo[(i, can_buy)]


        return backtrack(0, True, {})

