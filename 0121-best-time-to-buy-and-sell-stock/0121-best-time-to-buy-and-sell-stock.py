class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l , r = 0 , 1 # means start from day 1 and day 2
        maxPro = 0 
        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l] #means sell - buy = profit
                maxPro = max(maxPro , profit)
            else:
                l = r #means left takes place of right
            r += 1
        return maxPro

        