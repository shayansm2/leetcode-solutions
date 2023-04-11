from functools import lru_cache


class Solution:
    def mincostTickets(self, days: list[int], costs: list[int]) -> int:
        self.days = days
        self.costs = costs
        return self._get_cost(self.days[-1])

    @lru_cache(None)
    def _get_cost(self, day: int) -> int:
        if day < 1:
            return 0

        if day not in self.days:
            return self._get_cost(day - 1)

        one_day_ago_cost = self._get_cost(day - 1) if day >= 1 else 0
        one_week_ago_cost = self._get_cost(day - 7) if day >= 7 else 0
        one_month_age_cost = self._get_cost(day - 30) if day >= 30 else 0

        return min(
            one_day_ago_cost + self.costs[0],
            one_week_ago_cost + self.costs[1],
            one_month_age_cost + self.costs[2]
        )
