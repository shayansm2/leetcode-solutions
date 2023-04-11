class Solution:
    def mincostTickets(self, days: list[int], costs: list[int]) -> int:
        dp = []
        index = 0
        for day in range(days[-1]):
            one_day_ago_cost = dp[day - 1] if day >= 1 else 0
            one_week_ago_cost = dp[day - 7] if day >= 7 else 0
            one_month_age_cost = dp[day - 30] if day >= 30 else 0

            need_ticket = day == days[index] - 1

            if need_ticket:
                dp.append(min(
                    one_day_ago_cost + (costs[0] * need_ticket),
                    one_week_ago_cost + (costs[1] * need_ticket),
                    one_month_age_cost + (costs[2] * need_ticket)
                ))
                index += 1
            else:
                dp.append(dp[-1] if dp else 0)

        return dp[-1]
