class Solution(object):
    def maxProfit(self, prices):
        a=prices[0]
        profit=0
        for price in prices:
            a=min(a,price)
            profit=max(profit,price-a)
        return profit