from functools import lru_cache


class Solution:
    def stoneGameII(self, piles: list[int]) -> int:
        self.piles = piles
        return self.stone_game(0, 2)[0]

    @lru_cache
    def stone_game(self, start_index: int, length: int) -> tuple:
        if start_index >= len(self.piles):
            return 0, 0

        if start_index + length >= len(self.piles):
            return sum(self.piles[start_index:]), 0

        # print(start_index, length)
        current_stones = 0
        my_stones = 0
        competitor_stones = 0

        for steps in range(length):
            current_index = start_index + steps
            if current_index >= len(self.piles):
                break
            current_stones += self.piles[current_index]
            next_stone_game_result = self.stone_game(current_index + 1, max((steps + 1) * 2, length))
            if next_stone_game_result[1] + current_stones > my_stones:
                my_stones = next_stone_game_result[1] + current_stones
                competitor_stones = next_stone_game_result[0]

        print(start_index, length, my_stones, competitor_stones)
        return my_stones, competitor_stones


print(Solution().stoneGameII([2, 7, 9, 4, 4]))
print(Solution().stoneGameII([1, 2, 3, 4, 5, 100]))
print(Solution().stoneGameII(
    [5255, 5172, 860, 6605, 1200, 9410, 1194, 9808, 9161, 3440, 1567, 4940, 9114, 5695, 1683, 9723, 2255, 3284, 5519,
     4432, 5509, 1211, 2222, 496, 5437, 7456, 7236, 8768, 6994, 7846, 6326, 7943, 2117, 9156, 7160, 9265, 7138, 2035,
     6232, 478, 412, 7464, 2432, 2607, 263, 2841, 6918, 2354, 5986, 3844]
))
print(Solution().stoneGameII(
    [6333, 2390, 2813, 5576, 4242, 8335, 9539, 9166, 608, 8764, 1590, 5323, 9810, 8633, 5356, 2267, 824, 3285, 7509,
     5872, 6243, 9436, 5711, 6159, 5831, 8165, 1483, 355, 8783, 7876, 9255, 8644, 2378, 9626, 9451, 3495, 1581, 9788,
     2257, 4653, 2128, 6682, 451, 9993, 8004, 4440, 5011, 2860, 1829, 9101, 348, 6896, 1513, 9138, 8089, 1083, 1432,
     7604, 4418, 9991, 9219, 7001, 7522, 3684, 1883]
))  # Time Limit Exceed
