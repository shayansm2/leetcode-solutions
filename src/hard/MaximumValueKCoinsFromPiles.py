class Solution:
    def maxValueOfCoins(self, piles: list[list[int]], k: int) -> int:
        piles_sum = []
        for pile in piles:
            prefix_sum = 0
            pile_sum = []
            for coins_in_last_pile in pile:
                prefix_sum += coins_in_last_pile
                pile_sum.append(prefix_sum)
            piles_sum.append(pile_sum)

        dp = []

        first_dp_row = [0]

        for selected_coin in range(1, min(k, len(piles_sum[0])) + 1):
            first_dp_row.append(piles_sum[0][selected_coin - 1])

        dp.append(first_dp_row)

        for pile_number in range(1, len(piles_sum)):
            dp_row = [0]

            for selected_coin in range(1, k + 1):
                max_val = 0

                # print('f(n=', pile_number, ',k=', selected_coin, ')')
                # selected_coin, pile_number
                for coins_in_last_pile in range(min(len(piles_sum[pile_number]), selected_coin) + 1):
                    if selected_coin - coins_in_last_pile >= len(dp[-1]):
                        continue

                    coins_sum_in_last_pile = piles_sum[pile_number][
                        coins_in_last_pile - 1] if coins_in_last_pile > 0 else 0
                    coins_sum_in_prev_piles = dp[-1][selected_coin - coins_in_last_pile]
                    new_val = coins_sum_in_last_pile + coins_sum_in_prev_piles

                    # print('coins_in_last_pile', coins_in_last_pile)
                    # print('coins_sum_in_last_pile', coins_sum_in_last_pile)
                    # print('coins_sum_in_prev_piles', coins_sum_in_prev_piles)
                    # print('new_val', new_val)
                    max_val = max(max_val, new_val)

                dp_row.append(max_val)

            dp.append(dp_row)

        # print(dp)
        return dp[-1][-1]


samples = [
    {'piles': [[1, 100, 3], [7, 8, 9]], 'k': 2, 'Output': 101},
    {'piles': [[1, 100, 3], [7, 8, 9]], 'k': 3, 'Output': 108},
    {'piles': [[1, 100, 3], [7, 8, 9]], 'k': 4, 'Output': 116},
    {'piles': [[100], [100], [100], [100], [100], [100], [1, 1, 1, 1, 1, 1, 700]], 'k': 7, 'Output': 706}
]

for sample in samples:
    print(Solution().maxValueOfCoins(sample['piles'], sample['k']))
