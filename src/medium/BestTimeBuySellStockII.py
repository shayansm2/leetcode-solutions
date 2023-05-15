class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buyIndex = 0
        sellIndex = None
        profit = 0

        arraySize = len(prices)

        for i in range(1, arraySize):
            if sellIndex is None: # we should buy
                if prices[i] < prices[buyIndex]:
                    buyIndex = i
                else:
                    sellIndex = i
                    # print('buy in', buyIndex)
            else: # we should sell
                if prices[i] > prices[sellIndex]:
                    sellIndex = i
                else:
                    # print('sell in', sellIndex)
                    profit += prices[sellIndex] - prices[buyIndex]
                    buyIndex = i
                    sellIndex = None

        if sellIndex is not None:
            profit += prices[sellIndex] - prices[buyIndex]

        return profit