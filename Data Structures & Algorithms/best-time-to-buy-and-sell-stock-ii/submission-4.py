class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0 #We initialise our profits to be zero, since we have no trades

        for i in range(1, len(prices)): #We run a loop from index 1 to the end
            if prices[i-1] < prices[i]: #We take this step to see if there is a profit possibility since we compare today's price to yesterday's 
                profit += prices[i] - prices[i-1] #We keep a tally of all profits
        return profit #Once we have evaluated at all prices, we return the final total possible profit
