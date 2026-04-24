class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_buy=1000
        max_profit=0
        for i in prices:
            if i < min_buy:
                min_buy=i
            current_profit=i-min_buy
            if current_profit > max_profit:
                max_profit=current_profit
        return max_profit