class Solution:
    def punishmentNumber(self, n: int) -> int:
        summation = 0
        for i in range(1, n + 1):
            if self.can_have_sum(str(i ** 2), i):
                summation += (i ** 2)
        return summation

    def can_have_sum(self, s: str, n: int) -> bool:
        if int(s) == n:
            return True

        if len(s) == 1:
            return int(s) == n

        for i in range(1, len(s)):
            new_number = int(s[:i])
            print(s, s[:i], new_number, n)
            if new_number > n:
                return False

            if self.can_have_sum(s[i:], n - new_number):
                return True

        return False


# print(Solution().can_have_sum(str(45*45), 45))
print(Solution().punishmentNumber(45))  # 3503
