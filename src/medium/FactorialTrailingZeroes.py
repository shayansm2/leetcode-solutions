class Solution:
    def trailingZeroes(self, n: int) -> int:
        trailing_zeroes = 0
        for i in range(1, n + 1):
            trailing_zeroes += self.get_number_of_five_factors(i)

        return trailing_zeroes

    def get_number_of_five_factors(self, number: int):
        if number % 5 != 0:
            return 0

        counter = 0

        while number % 5 == 0:
            counter += 1
            number /= 5

        return counter
