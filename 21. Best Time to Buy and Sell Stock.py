class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        best = 0 #this is max profit
        for i in range(0, len(prices)):
            min_price = min(min_price, i)
            best = max(best, i - min_price)
        return best

            