class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0
        min_price=prices[0]
        for p in prices[1:]:
            if p<min_price:
                min_price=p
            elif profit<p-min_price:
                profit=p-min_price
        return profit
            
        
        