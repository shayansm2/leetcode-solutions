class Solution:
    def __init__(self):
        self.modulo = 1000000007
        self.cache = dict()
        self.counter = 0

    def ways(self, pizza: list[str], k: int) -> int:
        self.counter += 1

        if self._get_input_hash(pizza, k) in self.cache:
            return self.cache[self._get_input_hash(pizza, k)]

        number_of_ways = self._calculate_number_of_ways(pizza, k)
        self.cache[self._get_input_hash(pizza, k)] = number_of_ways
        return number_of_ways

    def _calculate_number_of_ways(self, pizza: list[str], k: int) -> int:
        if k < 2:
            return 1

        row_apple_count = [0 for i in range(len(pizza))]
        column_apple_count = [0 for i in range(len(pizza[0]))]

        for row_number, row in enumerate(pizza):
            for column_number, item in enumerate(row):
                if item != 'A':
                    continue

                row_apple_count[row_number] += 1
                column_apple_count[column_number] += 1

        row_cumsum = []
        cumsum = 0
        for i in row_apple_count:
            cumsum += i
            row_cumsum.append(cumsum)

        column_cumsum = []
        cumsum = 0
        for i in column_apple_count:
            cumsum += i
            column_cumsum.append(cumsum)

        number_of_ways = 0

        for row_number, apple_sum in enumerate(row_cumsum):
            if apple_sum == 0:
                continue

            if row_cumsum[-1] - apple_sum == 0:
                break

            number_of_ways += (self.ways(self._cut_horizontally(pizza, row_number), k - 1) % self.modulo)
            number_of_ways %= self.modulo

        for column_number, apple_sum in enumerate(column_cumsum):
            if apple_sum == 0:
                continue

            if column_cumsum[-1] - apple_sum == 0:
                break

            number_of_ways += (self.ways(self._cut_vertically(pizza, column_number), k - 1) % self.modulo)
            number_of_ways %= self.modulo

        return number_of_ways

    @staticmethod
    def _cut_horizontally(pizza: list[str], row_number: int) -> list[str]:
        return pizza[row_number + 1:]

    @staticmethod
    def _cut_vertically(pizza: list[str], column_number: int) -> list[str]:
        new_pizza = []

        for row in pizza:
            new_pizza.append(row[column_number + 1:])

        return new_pizza

    @staticmethod
    def _get_input_hash(pizza: list[str], k: int) -> str:
        return '-'.join(pizza) + str(k)
