class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        j = 1
        profit = 0
        while j < len(prices):
            temp_profit = prices[j] - prices[i]
            profit = max(profit, temp_profit)
            if prices[j] < prices[i]:
                i = j 
            j += 1
        return profit
