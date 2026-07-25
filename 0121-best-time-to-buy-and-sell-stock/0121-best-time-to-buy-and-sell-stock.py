class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # Intialize the lowest price seen so far to infinity
        min_price = float('inf')
        max_profit = 0

        for price in prices:
            # Update min_price if the current price is new low
            if price < min_price:
                min_price = price

            # Otherwise, check how much profit we would make if we sold today
            elif price - min_price > max_profit:
                max_profit = price - min_price

        return max_profit