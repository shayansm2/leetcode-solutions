from typing import List


class BestTimeToBuyAndSellStock:
    def maxProfit(self, prices: List[int]) -> int:
        bestProfit = 0
        minIndex = 0

        for i in range(1, len(prices)):
            if prices[i] < prices[minIndex]:
                minIndex = i

            bestProfit = max(bestProfit, prices[i] - prices[minIndex])

        return bestProfit
