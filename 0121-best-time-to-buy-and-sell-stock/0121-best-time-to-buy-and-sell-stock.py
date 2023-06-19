class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0
        min_prices=prices[0]
        for p in prices[1:]:
            if p<min_prices:
                min_prices=p
            elif profit<p-min_prices:
                profit=p-min_prices
        return profit