class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_prof=0
        min_buy=float('inf')
        for price in prices:
            min_buy=min(min_buy,price)
            max_prof=max(max_prof,price-min_buy)
        return max_prof