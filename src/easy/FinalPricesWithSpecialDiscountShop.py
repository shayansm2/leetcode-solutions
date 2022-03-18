from typing import List


class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        length = len(prices)
        answer = []

        for i in range(0, length - 1):
            price = prices[i]
            discount = 0

            for j in range(i + 1, length):
                if prices[j] <= prices[i]:
                    discount = prices[j]
                    break

            answer.append(price - discount)

        answer.append(prices[-1])
        return answer


print(Solution().finalPrices([8, 4, 6, 2, 3]))
