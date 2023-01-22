class Solution:
    def alternateDigitSum(self, n: int) -> int:
        digitSum = 0
        index = -1

        while n > 0:
            index += 1
            digit = n % 10

            digitSum += (((-1) ** index) * digit)
            n = n // 10

        return digitSum * ((-1) ** (index))