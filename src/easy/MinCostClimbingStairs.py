from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0, 0]

        for i in range(2, len(cost)):
            dp.append(min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2]))

        n = len(cost)
        return min(dp[n - 1] + cost[n - 1], dp[n - 2] + cost[n - 2])