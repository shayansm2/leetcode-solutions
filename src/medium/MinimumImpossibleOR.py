class Solution:
    def minImpossibleOR(self, nums: list[int]) -> int:
        for n in range(31):
            # print((2**n) in nums, (2**n))
            if (2 ** n) not in nums:
                return 2 ** n
        return 1
