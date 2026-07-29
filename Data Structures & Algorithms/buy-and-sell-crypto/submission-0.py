class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        profit = 0
        buy = 0

        for i, p in enumerate(prices):
            if i == 0: continue
            temp = p - prices[buy]
            
            if temp > profit:
                profit = temp

            if prices[buy] > p:
                buy = i
        
        return profit