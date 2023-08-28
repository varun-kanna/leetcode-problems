class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        minimum = prices[0]
        for price in prices:
            if price < minimum:
                minimum = price
            profit = max(profit, price-minimum)
        return profit