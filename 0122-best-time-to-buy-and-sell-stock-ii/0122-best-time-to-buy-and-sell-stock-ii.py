class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_total_profit = 0
        
        # Start looping from the second day 
        for i in range(1, len(prices)):
            # If today's price is higher than yesterday's price
            if prices[i] > prices[i-1]:
                # Collect the profit immediatly
                max_total_profit += prices[i] - prices[i-1]

        return max_total_profit