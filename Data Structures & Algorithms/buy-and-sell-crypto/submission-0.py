class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit = 0
        a = 0
        b = a + 1
        while b < len(prices) and a < len(prices):
            profit = prices[b] - prices[a]
            maxprofit = max(maxprofit, profit)
            if prices[a] > prices[b]:
                a = b
                b = a + 1
            else:
                b += 1
        return maxprofit
            