class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        if len(prices)<2: return 0
        
        buy = prices[0]
        sell = None
        globprofit = 0
        for iprice in prices[1:]:
            profit = iprice-buy
            globprofit = max(globprofit, profit)
            if profit>0:
                sell = iprice
            else:
                buy = iprice
                
        return globprofit
                
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        glob = 0
        for i in range(len(prices)):
            for j in range(i+1,len(prices)):
                glob = max(glob,prices[j]-prices[i])
        return glob

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        glob = 0
        buy = prices[0]
        for sell in prices[1:]:
            glob = max(glob,sell-buy)
            if sell<buy:
                buy = sell
        return glob