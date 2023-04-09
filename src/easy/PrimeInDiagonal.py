class Solution:
    def diagonalPrime(self, nums: list[list[int]]) -> int:
        largest_prime = 0

        for i in range(len(nums)):
            if self.is_prime(nums[i][i]):
                largest_prime = max(largest_prime, nums[i][i])
            if self.is_prime(nums[i][len(nums) - i - 1]):
                largest_prime = max(largest_prime, nums[i][len(nums) - i - 1])

        return largest_prime

    def is_prime(self, num: int):
        if num < 2:
            return False

        i = 2
        while i ** 2 <= num:
            if num % i == 0:
                return False
            i += 1
        return True
